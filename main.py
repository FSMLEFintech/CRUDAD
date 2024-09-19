import tkinter as tk
from tkinter import ttk
from clientes import ClientesApp
from empleados import EmpleadosApp
from insumos import InsumosApp

class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión Veterinaria")
        self.root.geometry("400x300")
        self.root.resizable(False, False)

        # Botones para abrir los CRUDs
        ttk.Button(self.root, text="Gestión de Clientes", command=self.abrir_gestion_clientes).pack(pady=10)
        ttk.Button(self.root, text="Gestión de Empleados", command=self.abrir_gestion_empleados).pack(pady=10)
        ttk.Button(self.root, text="Gestión de Insumos", command=self.abrir_gestion_insumos).pack(pady=10)

    def abrir_gestion_clientes(self):
        self.root.destroy()
        root_clientes = tk.Tk()
        app_clientes = ClientesApp(root_clientes)
        root_clientes.mainloop()

    def abrir_gestion_empleados(self):
        self.root.destroy()
        root_empleados = tk.Tk()
        app_empleados = EmpleadosApp(root_empleados)
        root_empleados.mainloop()

    def abrir_gestion_insumos(self):
        self.root.destroy()
        root_insumos = tk.Tk()
        app_insumos = InsumosApp(root_insumos, self.mostrar_menu_principal)
        root_insumos.mainloop()

    def mostrar_menu_principal(self):
        root = tk.Tk()
        app = MainApp(root)
        root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()
