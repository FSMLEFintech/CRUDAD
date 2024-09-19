import tkinter as tk
from tkinter import ttk, messagebox
from agregar import agregar_cliente
from listar import listar_clientes
from editar import editar_cliente
from eliminar import eliminar_cliente
from database import crear_tablas


class ClientesApp:
    def __init__(self, root, main_app_callback=None):
        self.root = root
        self.main_app_callback = main_app_callback  # Callback para regresar al menú principal
        self.root.title("Gestión de Clientes")
        self.root.geometry("800x500")
        self.root.resizable(False, False)

        # Crear todas las tablas (clientes, cursos, empleados)
        crear_tablas()

        # Crear el contenedor para la interfaz
        self.frame = ttk.Frame(self.root)
        self.frame.pack(pady=20)

        # Variables para el formulario
        self.nombre = tk.StringVar()
        self.direccion = tk.StringVar()
        self.telefono = tk.StringVar()
        self.orden = tk.StringVar()

        # Crear las entradas de texto
        ttk.Label(self.frame, text="Nombre").grid(row=0, column=0, padx=10, pady=10)
        ttk.Entry(self.frame, textvariable=self.nombre, width=30).grid(row=0, column=1)

        ttk.Label(self.frame, text="Dirección").grid(row=1, column=0, padx=10, pady=10)
        ttk.Entry(self.frame, textvariable=self.direccion, width=30).grid(row=1, column=1)

        ttk.Label(self.frame, text="Teléfono").grid(row=2, column=0, padx=10, pady=10)
        ttk.Entry(self.frame, textvariable=self.telefono, width=30).grid(row=2, column=1)

        ttk.Label(self.frame, text="Orden").grid(row=3, column=0, padx=10, pady=10)
        ttk.Entry(self.frame, textvariable=self.orden, width=30).grid(row=3, column=1)

        # Botón para agregar cliente
        ttk.Button(self.frame, text="Agregar Cliente", command=self.agregar).grid(row=4, column=1, pady=20)

        # Crear tabla para mostrar los clientes
        self.tree = ttk.Treeview(self.root, columns=("ID", "Nombre", "Dirección", "Teléfono", "Orden"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("Dirección", text="Dirección")
        self.tree.heading("Teléfono", text="Teléfono")
        self.tree.heading("Orden", text="Orden")
        self.tree.column("ID", width=50)
        self.tree.column("Nombre", width=150)
        self.tree.column("Dirección", width=200)
        self.tree.column("Teléfono", width=100)
        self.tree.column("Orden", width=100)
        self.tree.pack(pady=20)

        # Botón para regresar al menú principal
        ttk.Button(self.frame, text="Regresar a Menú Principal", command=self.regresar_menu_principal).grid(row=5, column=1, pady=10)

        # Mostrar los clientes al iniciar
        self.mostrar_clientes()

    def regresar_menu_principal(self):
        self.root.destroy()  # Cerrar la ventana actual
        if self.main_app_callback:
            self.main_app_callback()  # Llamar a la función del menú principal

    def agregar(self):
        nombre = self.nombre.get()
        direccion = self.direccion.get()
        telefono = self.telefono.get()
        orden = self.orden.get()

        if nombre and direccion and telefono and orden:
            agregar_cliente(nombre, direccion, telefono, orden)
            messagebox.showinfo("Éxito", f"Cliente '{nombre}' agregado con éxito.")
            self.mostrar_clientes()  # Actualizar la lista
        else:
            messagebox.showwarning("Advertencia", "Todos los campos son obligatorios.")

    def mostrar_clientes(self):
        # Limpiar la tabla antes de actualizarla
        for row in self.tree.get_children():
            self.tree.delete(row)

        # Obtener los clientes de la base de datos
        clientes = listar_clientes()

        if not clientes:
            messagebox.showinfo("Información", "No hay clientes en la base de datos.")
        else:
            for cliente in clientes:
                self.tree.insert("", tk.END, values=cliente)

    def editar(self):
        try:
            selected_item = self.tree.selection()[0]  # Obtener el elemento seleccionado
            cliente_id = self.tree.item(selected_item)['values'][0]

            # Ventana emergente para editar el cliente
            edit_window = tk.Toplevel(self.root)
            edit_window.title("Editar Cliente")
            edit_window.geometry("300x250")
            edit_window.resizable(False, False)

            # Variables de edición
            nuevo_nombre = tk.StringVar(value=self.tree.item(selected_item)['values'][1])
            nueva_direccion = tk.StringVar(value=self.tree.item(selected_item)['values'][2])
            nuevo_telefono = tk.StringVar(value=self.tree.item(selected_item)['values'][3])
            nueva_orden = tk.StringVar(value=self.tree.item(selected_item)['values'][4])

            # Entradas de edición
            ttk.Label(edit_window, text="Nombre").pack(pady=10)
            ttk.Entry(edit_window, textvariable=nuevo_nombre, width=30).pack(pady=5)

            ttk.Label(edit_window, text="Dirección").pack(pady=10)
            ttk.Entry(edit_window, textvariable=nueva_direccion, width=30).pack(pady=5)

            ttk.Label(edit_window, text="Teléfono").pack(pady=10)
            ttk.Entry(edit_window, textvariable=nuevo_telefono, width=30).pack(pady=5)

            ttk.Label(edit_window, text="Orden").pack(pady=10)
            ttk.Entry(edit_window, textvariable=nueva_orden, width=30).pack(pady=5)

            # Botón para confirmar la edición
            def confirmar_edicion():
                editar_cliente(cliente_id, nuevo_nombre.get(), nueva_direccion.get(), nuevo_telefono.get(), nueva_orden.get())
                messagebox.showinfo("Éxito", "Cliente actualizado con éxito.")
                self.mostrar_clientes()  # Actualizar la lista
                edit_window.destroy()

            ttk.Button(edit_window, text="Confirmar", command=confirmar_edicion).pack(pady=20)

        except IndexError:
            messagebox.showwarning("Advertencia", "Por favor, selecciona un cliente para editar.")

    def eliminar(self):
        try:
            selected_item = self.tree.selection()[0]  # Obtener el elemento seleccionado
            cliente_id = self.tree.item(selected_item)['values'][0]
            eliminar_cliente(cliente_id)
            messagebox.showinfo("Éxito", f"Cliente con ID {cliente_id} eliminado con éxito.")
            self.mostrar_clientes()  # Actualizar la lista
        except IndexError:
            messagebox.showwarning("Advertencia", "Por favor, selecciona un cliente para eliminar.")


if __name__ == "__main__":
    # Crear las tablas de clientes, cursos y empleados si no existen
    crear_tablas()

    # Inicializar la interfaz de usuario
    root = tk.Tk()
    app = ClientesApp(root)
    root.mainloop()
