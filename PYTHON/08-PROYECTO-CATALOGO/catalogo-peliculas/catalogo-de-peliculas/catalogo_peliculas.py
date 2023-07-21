import tkinter as tk
from tkinter import ttk

from client.gui_app import Frame, barra_menu


def main():
    # CREACION DE LA VENTANA QUE SERÁ LA INTERFAZ DE USUARIO
    root = tk.Tk()
    root.title('Catálogo de Películas')
    root.iconbitmap('img/cp-logo.ico')
    root.resizable(1, 1)
    barra_menu(root)

# CREACIÓN DE UN FRAME QUE ES UN CONTENEDOR DE OBJETOS PARA DARLE LA APARIENCIA QUE QUEREMOS
    app = Frame(root=root)

    app.mainloop()


if __name__ == '__main__':
    main()
