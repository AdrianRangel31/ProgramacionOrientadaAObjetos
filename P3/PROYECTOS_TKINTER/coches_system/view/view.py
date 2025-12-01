import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def aplicar_estilos():
    style = ttk.Style()
    style.theme_use('clam')
    bg_color = "#f0f0f0"
    primary_color = "#4a90e2"
    secondary_color = "#e0e0e0"
    text_color = "#333333"

    style.configure(".", background=bg_color, foreground=text_color, font=("Helvetica", 10))
    style.configure("TFrame", background=bg_color)
    style.configure("TLabel", background=bg_color, foreground=text_color)
    style.configure("TButton", background=primary_color, foreground="white", padding=6, borderwidth=0)
    style.map("TButton", background=[('active', '#357abd')])
    style.configure("Treeview", background="white", fieldbackground="white", foreground=text_color, rowheight=25)
    style.configure("Treeview.Heading", background=secondary_color, foreground=text_color, font=("Helvetica", 10, "bold"))
    style.map("Treeview", background=[('selected', primary_color)], foreground=[('selected', 'white')])
    style.configure("Header.TLabel", font=("Helvetica", 16, "bold"), padding=10)

class MenuView(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.setup_ui()

    def setup_ui(self):
        frame_central = ttk.Frame(self)
        frame_central.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        ttk.Label(frame_central, text="Menú Principal", style="Header.TLabel").pack(pady=20)
        
        ttk.Button(frame_central, text="Gestionar Coches", command=lambda: self.controller.show_view("coches")).pack(pady=10, fill=tk.X, ipadx=20)
        ttk.Button(frame_central, text="Gestionar Camionetas", command=lambda: self.controller.show_view("camionetas")).pack(pady=10, fill=tk.X)
        ttk.Button(frame_central, text="Gestionar Camiones", command=lambda: self.controller.show_view("camiones")).pack(pady=10, fill=tk.X)
        ttk.Button(frame_central, text="Salir", command=self.controller.salir).pack(pady=20, fill=tk.X)

class BaseCrudView(ttk.Frame):
    def __init__(self, parent, controller, titulo, columnas_config):
        super().__init__(parent)
        self.controller = controller
        self.columnas_config = columnas_config
        self.entries = {}
        self.selected_id = None
        self.setup_ui(titulo)

    def setup_ui(self, titulo):
        # Header
        header = ttk.Frame(self)
        header.pack(fill=tk.X)
        ttk.Button(header, text="< Menú", command=self.controller.go_back).pack(side=tk.LEFT, padx=10, pady=10)
        ttk.Label(header, text=titulo, style="Header.TLabel").pack(side=tk.LEFT)

        # Formulario
        form = ttk.LabelFrame(self, text="Registro", padding=10)
        form.pack(fill=tk.X, padx=20, pady=10)
        
        r, c = 0, 0
        for col in self.columnas_config:
            if col['name'] == 'ID': continue # ID autogenerado
            ttk.Label(form, text=col['label']).grid(row=r, column=c, sticky=tk.W, padx=5, pady=5)
            
            if col.get('type') == 'combobox':
                e = ttk.Combobox(form, values=col.get('values'), state="readonly")
            else:
                e = ttk.Entry(form)
            
            e.grid(row=r, column=c+1, sticky=tk.EW, padx=5, pady=5)
            self.entries[col['name']] = e
            
            c += 2
            if c >= 4: # 2 columnas visuales
                c = 0
                r += 1
        form.columnconfigure((1, 3), weight=1)

        # Botones
        btns = ttk.Frame(self)
        btns.pack(fill=tk.X, padx=20, pady=10)
        ttk.Button(btns, text="Agregar", command=self.add).pack(side=tk.LEFT, padx=5)
        ttk.Button(btns, text="Modificar", command=self.mod).pack(side=tk.LEFT, padx=5)
        ttk.Button(btns, text="Eliminar", command=self.dele).pack(side=tk.LEFT, padx=5)
        ttk.Button(btns, text="Limpiar", command=self.clear).pack(side=tk.RIGHT, padx=5)

        # Tabla
        tree_f = ttk.Frame(self)
        tree_f.pack(fill=tk.BOTH, expand=True, padx=20, pady=(0, 20))
        cols = [c['name'] for c in self.columnas_config]
        self.tree = ttk.Treeview(tree_f, columns=cols, show="headings")
        
        sb_y = ttk.Scrollbar(tree_f, orient=tk.VERTICAL, command=self.tree.yview)
        sb_x = ttk.Scrollbar(tree_f, orient=tk.HORIZONTAL, command=self.tree.xview)
        self.tree.configure(yscroll=sb_y.set, xscroll=sb_x.set)
        
        sb_y.pack(side=tk.RIGHT, fill=tk.Y)
        sb_x.pack(side=tk.BOTTOM, fill=tk.X)
        self.tree.pack(fill=tk.BOTH, expand=True)
        
        for col in self.columnas_config:
            self.tree.heading(col['name'], text=col['label'])
            self.tree.column(col['name'], width=90, anchor=tk.CENTER)
        
        self.tree.bind("<<TreeviewSelect>>", self.on_select)

    def on_select(self, e):
        sel = self.tree.selection()
        if sel:
            vals = self.tree.item(sel[0])['values']
            self.selected_id = vals[0]
            idx = 1
            for col in self.columnas_config:
                if col['name'] == 'ID': continue
                if col['name'] in self.entries:
                    self.entries[col['name']].delete(0, tk.END)
                    self.entries[col['name']].insert(0, vals[idx])
                idx += 1

    def get_data(self):
        d = []
        for col in self.columnas_config:
            if col['name'] == 'ID': continue
            v = self.entries[col['name']].get()
            if not v:
                messagebox.showwarning("Faltan datos", f"El campo {col['label']} es obligatorio")
                return None
            d.append(v)
        return tuple(d)

    def clear(self):
        self.selected_id = None
        self.tree.selection_remove(self.tree.selection())
        for e in self.entries.values():
            e.delete(0, tk.END)
            if isinstance(e, ttk.Combobox): e.set('')

    def add(self): self.controller.agregar(self.get_data())
    def mod(self): self.controller.modificar(self.selected_id, self.get_data())
    def dele(self): self.controller.eliminar(self.selected_id)

    def update_treeView(self, data):
        self.clear()
        for i in self.tree.get_children(): self.tree.delete(i)
        for r in data: self.tree.insert("", tk.END, values=r)

class CochesView(BaseCrudView):
    def __init__(self, parent, controller):
        cols = [
            {'name': 'ID', 'label': 'ID'},
            {'name': 'Color', 'label': 'Color'},
            {'name': 'Marca', 'label': 'Marca'},
            {'name': 'Modelo', 'label': 'Modelo'},
            {'name': 'Velocidad', 'label': 'Velocidad'},
            {'name': 'Caballaje', 'label': 'Caballaje'},
            {'name': 'Plazas', 'label': 'Plazas'},
        ]
        super().__init__(parent, controller, "Gestión de Coches", cols)

class CamionetasView(BaseCrudView):
    def __init__(self, parent, controller):
        cols = [
            {'name': 'ID', 'label': 'ID'},
            {'name': 'Marca', 'label': 'Marca'},
            {'name': 'Color', 'label': 'Color'},
            {'name': 'Modelo', 'label': 'Modelo'},
            {'name': 'Velocidad', 'label': 'Velocidad'},
            {'name': 'Caballaje', 'label': 'Caballaje'},
            {'name': 'Plazas', 'label': 'Plazas'},
            {'name': 'Traccion', 'label': 'Tracción'},
            {'name': 'Cerrada', 'label': 'Cerrada (1=Sí/0=No)', 'type': 'combobox', 'values': ['1', '0']},
        ]
        super().__init__(parent, controller, "Gestión de Camionetas", cols)

class CamionesView(BaseCrudView):
    def __init__(self, parent, controller):
        cols = [
            {'name': 'ID', 'label': 'ID'},
            {'name': 'Color', 'label': 'Color'},
            {'name': 'Marca', 'label': 'Marca'},
            {'name': 'Modelo', 'label': 'Modelo'},
            {'name': 'Velocidad', 'label': 'Velocidad'},
            {'name': 'Caballaje', 'label': 'Caballaje'},
            {'name': 'Plazas', 'label': 'Plazas'},
            {'name': 'Eje', 'label': 'Ejes'},
            {'name': 'Capacidad', 'label': 'Capacidad'},
        ]
        super().__init__(parent, controller, "Gestión de Camiones", cols)