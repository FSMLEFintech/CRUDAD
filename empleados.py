import tkinter as tk
from tkinter import ttk, messagebox
from agregar import agregar_empleado
from listar import listar_empleados
from editar import editar_empleado
from eliminar import eliminar_empleado
from database import crear_tablas

class EmpleadosApp:
    def __init__(self, root, main_app_callback=None):
        self.root = root
        self.main_app_callback = main_app_callback
        self.root.title("Gestión de Empleados")
        self.root.geometry("800x500")
        self.root.resizable(False, False)

        # Crear todas las tablas (clientes, empleados, insumos)
        crear_tablas()

        # Crear el contenedor para la interfaz
        self.frame = ttk.Frame(self.root)
        self.frame.pack(pady=20)

        # Variables para el formulario
        self.nombre = tk.StringVar()
        self.puesto = tk.StringVar()
        self.salario = tk.StringVar()

        # Crear las entradas de texto
        ttk.Label(self.frame, text="Nombre").grid(row=0, column=0, padx=10, pady=10)
        ttk.Entry(self.frame, textvariable=self.nombre, width=30).grid(row=0, column=1)

        ttk.Label(self.frame, text="Puesto").grid(row=1, column=0, padx=10, pady=10)
        ttk.Entry(self.frame, textvariable=self.puesto, width=30).grid(row=1, column=1)

        ttk.Label(self.frame, text="Salario").grid(row=2, column=0, padx=10, pady=10)
        ttk.Entry(self.frame, textvariable=self.salario, width=30).grid(row=2, column=1)

        # Botón para agregar empleado
        ttk.Button(self.frame, text="Agregar Empleado", command=self.agregar).grid(row=3, column=1, pady=20)

        # Crear tabla para mostrar los empleados
        self.tree = ttk.Treeview(self.root, columns=("ID", "Nombre", "Puesto", "Salario"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("Puesto", text="Puesto")
        self.tree.heading("Salario", text="Salario")
        self.tree.column("ID", width=50)
        self.tree.column("Nombre", width=150)
        self.tree.column("Puesto", width=150)
        self.tree.column("Salario", width=100)
        self.tree.pack(pady=20)

        # Botón para regresar al menú principal
        ttk.Button(self.frame, text="Regresar a Menú Principal", command=self.regresar_menu_principal).grid(row=4, column=1, pady=10)

        # Mostrar los empleados al iniciar
        self.mostrar_empleados()

    def regresar_menu_principal(self):
        self.root.destroy()
        if self.main_app_callback:
            self.main_app_callback()

    def agregar(self):
        nombre = self.nombre.get()
        puesto = self.puesto.get()
        salario = self.salario.get()

        if nombre and puesto and salario:
            agregar_empleado(nombre, puesto, salario)
            messagebox.showinfo("Éxito", f"Empleado '{nombre}' agregado con éxito.")
            self.mostrar_empleados()
        else:
            messagebox.showwarning("Advertencia", "Todos los campos son obligatorios.")

    def mostrar_empleados(self):
        for row in self.tree.get_children():
            self.tree.delete(row)

        empleados = listar_empleados()

        if not empleados:
            messagebox.showinfo("Información", "No hay empleados en la base de datos.")
        else:
            for empleado in empleados:
                self.tree.insert("", tk.END, values=empleado)

    def editar(self):
        try:
            selected_item = self.tree.selection()[0]
            empleado_id = self.tree.item(selected_item)['values'][0]

            edit_window = tk.Toplevel(self.root)
            edit_window.title("Editar Empleado")
            edit_window.geometry("300x250")
            edit_window.resizable(False, False)

            nuevo_nombre = tk.StringVar(value=self.tree.item(selected_item)['values'][1])
            nuevo_puesto = tk.StringVar(value=self.tree.item(selected_item)['values'][2])
            nuevo_salario = tk.StringVar(value=self.tree.item(selected_item)['values'][3])

            ttk.Label(edit_window, text="Nombre").pack(pady=10)
            ttk.Entry(edit_window, textvariable=nuevo_nombre, width=30).pack(pady=5)

            ttk.Label(edit_window, text="Puesto").pack(pady=10)
            ttk.Entry(edit_window, textvariable=nuevo_puesto, width=30).pack(pady=5)

            ttk.Label(edit_window, text="Salario").pack(pady=10)
            ttk.Entry(edit_window, textvariable=nuevo_salario, width=30).pack(pady=5)

            def confirmar_edicion():
                editar_empleado(empleado_id, nuevo_nombre.get(), nuevo_puesto.get(), nuevo_salario.get())
                messagebox.showinfo("Éxito", "Empleado actualizado con éxito.")
                self.mostrar_empleados()
                edit_window.destroy()

            ttk.Button(edit_window, text="Confirmar", command=confirmar_edicion).pack(pady=20)

        except IndexError:
            messagebox.showwarning("Advertencia", "Por favor, selecciona un empleado para editar.")

    def eliminar(self):
        try:
            selected_item = self.tree.selection()[0]
            empleado_id = self.tree.item(selected_item)['values'][0]
            eliminar_empleado(empleado_id)
            messagebox.showinfo("Éxito", f"Empleado con ID {empleado_id} eliminado con éxito.")
            self.mostrar_empleados()
        except IndexError:
            messagebox.showwarning("Advertencia", "Por favor, selecciona un empleado para eliminar.")


if __name__ == "__main__":
    crear_tablas()
    root = tk.Tk()
    app = EmpleadosApp(root)
    root.mainloop()
