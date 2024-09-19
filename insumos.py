import tkinter as tk
from tkinter import ttk, messagebox
from database import conectar

# Crear la tabla de insumos si no existe
def crear_tabla_insumos():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS insumos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            proveedor TEXT NOT NULL,
            cantidad INTEGER NOT NULL,
            costo REAL NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def agregar_insumo(nombre, proveedor, cantidad, costo):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO insumos (nombre, proveedor, cantidad, costo)
        VALUES (?, ?, ?, ?)
    ''', (nombre, proveedor, cantidad, costo))
    conn.commit()
    conn.close()

def listar_insumos():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM insumos')
    insumos = cursor.fetchall()
    conn.close()
    return insumos

def eliminar_insumo(id_insumo):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM insumos WHERE id = ?', (id_insumo,))
    conn.commit()
    conn.close()

def editar_insumo(id_insumo, nuevo_nombre, nuevo_proveedor, nueva_cantidad, nuevo_costo):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE insumos
        SET nombre = ?, proveedor = ?, cantidad = ?, costo = ?
        WHERE id = ?
    ''', (nuevo_nombre, nuevo_proveedor, nueva_cantidad, nuevo_costo, id_insumo))
    conn.commit()
    conn.close()

class InsumosApp:
    def __init__(self, root, regresar_func):
        self.root = root
        self.root.title("Gestión de Insumos")
        self.root.geometry("800x500")
        self.root.resizable(False, False)

        # Variables para el formulario de insumos
        self.nombre = tk.StringVar()
        self.proveedor = tk.StringVar()
        self.cantidad = tk.IntVar()
        self.costo = tk.DoubleVar()

        # Crear las entradas de texto
        ttk.Label(self.root, text="Nombre").grid(row=0, column=0, padx=10, pady=10)
        ttk.Entry(self.root, textvariable=self.nombre, width=30).grid(row=0, column=1)

        ttk.Label(self.root, text="Proveedor").grid(row=1, column=0, padx=10, pady=10)
        ttk.Entry(self.root, textvariable=self.proveedor, width=30).grid(row=1, column=1)

        ttk.Label(self.root, text="Cantidad").grid(row=2, column=0, padx=10, pady=10)
        ttk.Entry(self.root, textvariable=self.cantidad, width=30).grid(row=2, column=1)

        ttk.Label(self.root, text="Costo").grid(row=3, column=0, padx=10, pady=10)
        ttk.Entry(self.root, textvariable=self.costo, width=30).grid(row=3, column=1)

        # Botón para agregar insumo
        ttk.Button(self.root, text="Agregar Insumo", command=self.agregar).grid(row=4, column=1, pady=20)

        # Crear tabla para mostrar los insumos
        self.tree = ttk.Treeview(self.root, columns=("ID", "Nombre", "Proveedor", "Cantidad", "Costo"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("Proveedor", text="Proveedor")
        self.tree.heading("Cantidad", text="Cantidad")
        self.tree.heading("Costo", text="Costo")
        self.tree.column("ID", width=50)
        self.tree.column("Nombre", width=150)
        self.tree.column("Proveedor", width=200)
        self.tree.column("Cantidad", width=100)
        self.tree.column("Costo", width=100)

        # Empaquetar la tabla dentro de un Frame y usar grid para que todo quede visible
        self.table_frame = ttk.Frame(self.root)
        self.table_frame.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

        self.tree.pack(in_=self.table_frame)

        # Botón para regresar al menú principal
        ttk.Button(self.root, text="Regresar a Menú Principal", command=regresar_func).grid(row=6, column=1, pady=10)

        # Mostrar los insumos al iniciar
        self.mostrar_insumos()

    def agregar(self):
        nombre = self.nombre.get()
        proveedor = self.proveedor.get()
        cantidad = self.cantidad.get()
        costo = self.costo.get()

        if nombre and proveedor and cantidad and costo:
            agregar_insumo(nombre, proveedor, cantidad, costo)
            messagebox.showinfo("Éxito", f"Insumo '{nombre}' agregado con éxito.")
            self.mostrar_insumos()  # Actualizar la lista
        else:
            messagebox.showwarning("Advertencia", "Todos los campos son obligatorios.")

    def mostrar_insumos(self):
        # Limpiar la tabla antes de actualizarla
        for row in self.tree.get_children():
            self.tree.delete(row)

        # Obtener los insumos de la base de datos
        insumos = listar_insumos()
        for insumo in insumos:
            self.tree.insert("", tk.END, values=insumo)

    def editar(self):
        try:
            selected_item = self.tree.selection()[0]  # Obtener el elemento seleccionado
            insumo_id = self.tree.item(selected_item)['values'][0]

            # Ventana emergente para editar el insumo
            edit_window = tk.Toplevel(self.root)
            edit_window.title("Editar Insumo")
            edit_window.geometry("300x250")
            edit_window.resizable(False, False)

            # Variables de edición
            nuevo_nombre = tk.StringVar(value=self.tree.item(selected_item)['values'][1])
            nuevo_proveedor = tk.StringVar(value=self.tree.item(selected_item)['values'][2])
            nueva_cantidad = tk.IntVar(value=self.tree.item(selected_item)['values'][3])
            nuevo_costo = tk.DoubleVar(value=self.tree.item(selected_item)['values'][4])

            # Entradas de edición
            ttk.Label(edit_window, text="Nombre").pack(pady=10)
            ttk.Entry(edit_window, textvariable=nuevo_nombre, width=30).pack(pady=5)

            ttk.Label(edit_window, text="Proveedor").pack(pady=10)
            ttk.Entry(edit_window, textvariable=nuevo_proveedor, width=30).pack(pady=5)

            ttk.Label(edit_window, text="Cantidad").pack(pady=10)
            ttk.Entry(edit_window, textvariable=nueva_cantidad, width=30).pack(pady=5)

            ttk.Label(edit_window, text="Costo").pack(pady=10)
            ttk.Entry(edit_window, textvariable=nuevo_costo, width=30).pack(pady=5)

            # Botón para confirmar la edición
            def confirmar_edicion():
                editar_insumo(insumo_id, nuevo_nombre.get(), nuevo_proveedor.get(), nueva_cantidad.get(), nuevo_costo.get())
                messagebox.showinfo("Éxito", "Insumo actualizado con éxito.")
                self.mostrar_insumos()  # Actualizar la lista
                edit_window.destroy()

            ttk.Button(edit_window, text="Confirmar", command=confirmar_edicion).pack(pady=20)

        except IndexError:
            messagebox.showwarning("Advertencia", "Por favor, selecciona un insumo para editar.")

    def eliminar(self):
        try:
            selected_item = self.tree.selection()[0]  # Obtener el elemento seleccionado
            insumo_id = self.tree.item(selected_item)['values'][0]
            eliminar_insumo(insumo_id)
            messagebox.showinfo("Éxito", f"Insumo con ID {insumo_id} eliminado con éxito.")
            self.mostrar_insumos()  # Actualizar la lista
        except IndexError:
            messagebox.showwarning("Advertencia", "Por favor, selecciona un insumo para eliminar.")


if __name__ == "__main__":
    # Crear la tabla de insumos si no existe
    crear_tabla_insumos()

    # Inicializar la interfaz de usuario
    root = tk.Tk()
    app = InsumosApp(root, lambda: print("Regresar al menú principal"))
    root.mainloop()
