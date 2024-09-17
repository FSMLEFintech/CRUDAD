import tkinter as tk
from tkinter import ttk, messagebox
root = tk.Tk()  # Para aplicar temas modernos
from agregar import agregar_curso
from listar import listar_cursos
from editar import editar_curso
from eliminar import eliminar_curso
from database import crear_tabla


class CursoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Cursos")
        self.root.geometry("800x500")
        self.root.resizable(False, False)

        # Aquí se eliminó la línea de set_theme porque no es compatible con tk.Tk()

        # Crear el contenedor para la interfaz
        self.frame = ttk.Frame(self.root)
        self.frame.pack(pady=20)

        # Variables para el formulario
        self.codigo = tk.StringVar()
        self.nombre = tk.StringVar()
        self.creditos = tk.IntVar()

        # Crear las entradas de texto
        ttk.Label(self.frame, text="Código").grid(row=0, column=0, padx=10, pady=10)
        ttk.Entry(self.frame, textvariable=self.codigo, width=30).grid(row=0, column=1)

        ttk.Label(self.frame, text="Nombre").grid(row=1, column=0, padx=10, pady=10)
        ttk.Entry(self.frame, textvariable=self.nombre, width=30).grid(row=1, column=1)

        ttk.Label(self.frame, text="Créditos").grid(row=2, column=0, padx=10, pady=10)
        ttk.Entry(self.frame, textvariable=self.creditos, width=30).grid(row=2, column=1)

        # Botón para agregar curso
        ttk.Button(self.frame, text="Agregar Curso", command=self.agregar).grid(row=3, column=1, pady=20)

        # Crear tabla para mostrar los cursos
        self.tree = ttk.Treeview(self.root, columns=("ID", "Código", "Nombre", "Créditos"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Código", text="Código")
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("Créditos", text="Créditos")
        self.tree.column("ID", width=50)
        self.tree.column("Código", width=150)
        self.tree.column("Nombre", width=200)
        self.tree.column("Créditos", width=100)
        self.tree.pack(pady=20)

        # Barra de herramientas
        toolbar = ttk.Frame(self.root)
        toolbar.pack(fill=tk.X)

        ttk.Button(toolbar, text="Editar Curso", command=self.editar).pack(side=tk.LEFT, padx=10, pady=10)
        ttk.Button(toolbar, text="Eliminar Curso", command=self.eliminar).pack(side=tk.LEFT, padx=10, pady=10)

        # Mostrar los cursos al iniciar
        self.mostrar_cursos()

    def agregar(self):
        codigo = self.codigo.get()
        nombre = self.nombre.get()
        creditos = self.creditos.get()

        if codigo and nombre and creditos:
            agregar_curso(codigo, nombre, creditos)
            messagebox.showinfo("Éxito", f"Curso '{nombre}' agregado con éxito.")
            self.mostrar_cursos()  # Actualizar la lista
        else:
            messagebox.showwarning("Advertencia", "Todos los campos son obligatorios.")

    def mostrar_cursos(self):
        # Limpiar la tabla antes de actualizarla
        for row in self.tree.get_children():
            self.tree.delete(row)

        # Obtener los cursos de la base de datos
        cursos = listar_cursos()
        for curso in cursos:
            self.tree.insert("", tk.END, values=curso)

    def editar(self):
        try:
            selected_item = self.tree.selection()[0]  # Obtener el elemento seleccionado
            curso_id = self.tree.item(selected_item)['values'][0]

            # Ventana emergente para editar el curso
            edit_window = tk.Toplevel(self.root)
            edit_window.title("Editar Curso")
            edit_window.geometry("300x250")
            edit_window.resizable(False, False)

            # Variables de edición
            nuevo_codigo = tk.StringVar(value=self.tree.item(selected_item)['values'][1])
            nuevo_nombre = tk.StringVar(value=self.tree.item(selected_item)['values'][2])
            nuevos_creditos = tk.IntVar(value=self.tree.item(selected_item)['values'][3])

            # Entradas de edición
            ttk.Label(edit_window, text="Código").pack(pady=10)
            ttk.Entry(edit_window, textvariable=nuevo_codigo, width=30).pack(pady=5)

            ttk.Label(edit_window, text="Nombre").pack(pady=10)
            ttk.Entry(edit_window, textvariable=nuevo_nombre, width=30).pack(pady=5)

            ttk.Label(edit_window, text="Créditos").pack(pady=10)
            ttk.Entry(edit_window, textvariable=nuevos_creditos, width=30).pack(pady=5)

            # Botón para confirmar la edición
            def confirmar_edicion():
                editar_curso(curso_id, nuevo_codigo.get(), nuevo_nombre.get(), nuevos_creditos.get())
                messagebox.showinfo("Éxito", "Curso actualizado con éxito.")
                self.mostrar_cursos()  # Actualizar la lista
                edit_window.destroy()

            ttk.Button(edit_window, text="Confirmar", command=confirmar_edicion).pack(pady=20)

        except IndexError:
            messagebox.showwarning("Advertencia", "Por favor, selecciona un curso para editar.")

    def eliminar(self):
        try:
            selected_item = self.tree.selection()[0]  # Obtener el elemento seleccionado
            curso_id = self.tree.item(selected_item)['values'][0]
            eliminar_curso(curso_id)
            messagebox.showinfo("Éxito", f"Curso con ID {curso_id} eliminado con éxito.")
            self.mostrar_cursos()  # Actualizar la lista
        except IndexError:
            messagebox.showwarning("Advertencia", "Por favor, selecciona un curso para eliminar.")


if __name__ == "__main__":
    # Crear la tabla de cursos si no existe
    crear_tabla()

    # Inicializar la interfaz de usuario
    root = tk.Tk()  # Usamos ThemedTk para aplicar el tema
    app = CursoApp(root)
    root.mainloop()
