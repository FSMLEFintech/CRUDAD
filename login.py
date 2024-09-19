import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from clientes import ClientesApp  # Asegúrate de importar ClientesApp o la ventana principal del CRUD

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Veterinaria - Login")
        self.root.geometry("400x500")
        self.root.resizable(False, False)

        # Cargar imagen del logo
        self.logo_image = Image.open("logo.jpg")  # Asignar a un atributo de clase
        self.logo_image = self.logo_image.resize((200, 200), Image.Resampling.LANCZOS)  # Usar LANCZOS
        self.logo = ImageTk.PhotoImage(self.logo_image)

        # Mostrar logo
        logo_label = ttk.Label(self.root, image=self.logo)
        logo_label.pack(pady=20)

        # Crear campo de entrada para el login (usuario)
        ttk.Label(self.root, text="Usuario").pack(pady=10)
        self.username = ttk.Entry(self.root)
        self.username.pack(pady=10)

        # Crear campo de entrada para la contraseña
        ttk.Label(self.root, text="Contraseña").pack(pady=10)
        self.password = ttk.Entry(self.root, show="*")
        self.password.pack(pady=10)

        # Botón de Login
        login_button = ttk.Button(self.root, text="Login", command=self.login)
        login_button.pack(pady=10)

        # Botón de Saltar Login
        skip_button = ttk.Button(self.root, text="Saltar Login", command=self.skip_login)
        skip_button.pack(pady=10)

    def login(self):
        username = self.username.get()
        password = self.password.get()
        print(f"Usuario: {username}, Contraseña: {password}")
        # Aquí puedes agregar la lógica para redirigir a la pantalla principal después del login

    def skip_login(self):
        # Lógica para saltar el login y redirigir a la pantalla principal
        self.root.destroy()
        main_root = tk.Tk()
        app = ClientesApp(main_root)  # Abre la ventana del CRUD de clientes
        main_root.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()
