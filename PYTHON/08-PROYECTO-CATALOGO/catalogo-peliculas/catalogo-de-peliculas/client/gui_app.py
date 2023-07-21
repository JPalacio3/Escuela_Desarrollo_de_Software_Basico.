
import tkinter as tk
from tkinter import ttk, messagebox
from model.pelicula_dao import crear_tabla, borrar_tabla
from model.pelicula_dao import Pelicula, guardar, listar, editar, eliminar


def barra_menu(root):
    barra_menu = tk.Menu(root)
    root.config(menu=barra_menu, width=300, height=300)

    # menu de inicio
    menu_inicio = tk.Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label='Inicio', menu=menu_inicio)

    # Submenús
    menu_inicio.add_command(label='Crear Tabla', command=crear_tabla)
    menu_inicio.add_command(label='Eliminar Tabla', command=borrar_tabla)
    menu_inicio.add_command(label='Salir', command=root.destroy)

    barra_menu.add_cascade(label='Consultar')
    barra_menu.add_cascade(label='Configuración')
    barra_menu.add_cascade(label='Ayuda')


class Frame(tk.Frame):

    def __init__(self, root=None):
        super().__init__(root, width=480, height=320)
        self.root = root
        self.pack()
        self.id_pelicula = None

        # Ejecutar los campos de peliculas
        self.tabla_peliculas()
        self.campos_pelicula()
        self.deshabilitar_campos()
        # self.habilitar_campos()

    def campos_pelicula(self):
        # Labels de cada campo
        self.label_nombre = tk.Label(self, text='Nombre: ')
        self.label_nombre.config(font=('Arial', 12, 'bold'))
        self.label_nombre.grid(row=0, column=0, padx=10, pady=10)

        self.label_duracion = tk.Label(self, text='Duración: ')
        self.label_duracion.config(font=('Arial', 12, 'bold'))
        self.label_duracion.grid(row=1, column=0, padx=10, pady=10)

        self.label_genero = tk.Label(self, text='Género: ')
        self.label_genero.config(font=('Arial', 12, 'bold'))
        self.label_genero.grid(row=2, column=0, padx=10, pady=10)

        # Campos de entrada ( Entries )
        #  NOMBRE
        self.nombre = tk.StringVar()
        self.entry_nombre = tk.Entry(self, textvariable=self.nombre)
        self.entry_nombre.config(
            width=50, font=('Arial', 12, 'bold'))
        self.entry_nombre.grid(row=0, column=1, padx=10, pady=10, columnspan=2)

        # DURACIÓN
        self.duracion = tk.StringVar()
        self.entry_duracion = tk.Entry(self, textvariable=self.duracion)
        self.entry_duracion.config(
            width=50, font=('Arial', 12, 'bold'))
        self.entry_duracion.grid(
            row=1, column=1, padx=10, pady=10, columnspan=2)

        # GÉNERO
        self.genero = tk.StringVar()
        self.entry_genero = tk.Entry(self, textvariable=self.genero)
        self.entry_genero.config(
            width=50, font=('Arial', 12, 'bold'))
        self.entry_genero.grid(row=2, column=1, padx=10, pady=10, columnspan=2)

        # Botones
        # Nuevo
        self.btn_nuevo = tk.Button(
            self, text='Nuevo', command=self.habilitar_campos)
        self.btn_nuevo.config(width=20, font=(
            'Arial', 12, 'bold'), fg='#DAD5D6', bg='#158645', cursor='hand2', activebackground='#35BD6F')
        self.btn_nuevo.grid(row=3, column=0, padx=10, pady=10)

        # Guardar
        self.btn_guardar = tk.Button(
            self, text='Guardar', command=self.guardar_datos)
        self.btn_guardar.config(width=20, font=(
            'Arial', 12, 'bold'), fg='#DAD5D6', bg='#1658A2', cursor='hand2', activebackground='#3586DF')
        self.btn_guardar.grid(row=3, column=1, padx=10, pady=10)

        # Cancelar
        self.btn_cancelar = tk.Button(
            self, text='Cancelar', command=self.deshabilitar_campos)
        self.btn_cancelar.config(width=20, font=(
            'Arial', 12, 'bold'), fg='#DAD5D6', bg='#BD152E', cursor='hand2', activebackground='#E15370')
        self.btn_cancelar.grid(row=3, column=2, padx=10, pady=10)

    # Métodos para habilitar y deshabilitar los campos
    def habilitar_campos(self):
        # Enviar datos vacíos al objeto para limpiar los campos
        self.nombre.set('')
        self.duracion.set('')
        self.genero.set('')

        # Habilitar los campos y los botones
        self.entry_nombre.config(state='normal')
        self.entry_duracion.config(state='normal')
        self.entry_genero.config(state='normal')

        self.btn_guardar.config(state='normal')
        self.btn_cancelar.config(state='normal')

    def deshabilitar_campos(self):
        # Enviar datos vacíos al objeto para limpiar los campos
        self.id_pelicula = None
        self.nombre.set('')
        self.duracion.set('')
        self.genero.set('')

        # Deshabilitar los campos y los botones
        self.entry_nombre.config(state='disabled')
        self.entry_duracion.config(state='disabled')
        self.entry_genero.config(state='disabled')

        self.btn_guardar.config(state='disabled')
        self.btn_cancelar.config(state='disabled')

    def guardar_datos(self):
        peliculas = Pelicula(
            self.nombre.get(),
            self.duracion.get(),
            self.genero.get(),
        )

        if self.id_pelicula == None:
            guardar(peliculas)
        else:
            editar(peliculas, self.id_pelicula)

        self.tabla_peliculas()

        self.deshabilitar_campos()

    def tabla_peliculas(self):
        # Recuperar la lista de peliculas
        self.lista_peliculas = listar()

        self.tabla = ttk.Treeview(self, column=(
            'Nombre,', 'Duración', 'Género'))
        self.tabla.grid(row=4, column=0, columnspan=4, sticky='nse')

        # Scrollbar para la teabla de si exede 10 registros
        self.scroll = ttk.Scrollbar(
            self, orient='vertical', command=self.tabla.yview)
        self.scroll.grid(row=4, column=4, sticky='nse')
        self.tabla.configure(yscrollcommand=self.scroll.set)

        self.tabla.heading('#0', text='ID')
        self.tabla.heading('#1', text='NOMBRE')
        self.tabla.heading('#2', text='DURACIÓN')
        self.tabla.heading('#3', text='GÉNERO')

        # Iterar en la lista de Peliculas
        for p in self.lista_peliculas:
            self.tabla.insert('', 0, text=p[0], values=(p[1], p[2], p[3]))

        # Botones de Actualizar y Eliminar
        # Actualizar
        self.btn_editar = tk.Button(
            self, text='Editar', command=self.editar_datos)
        self.btn_editar.config(width=20, font=(
            'Arial', 12, 'bold'), fg='#DAD5D6', bg='#158645', cursor='hand2', activebackground='#35BD6F')
        self.btn_editar.grid(row=5, column=1, padx=10, pady=10)

        # Cancelar
        # Cancelar
        self.btn_eliminar = tk.Button(
            self, text='Eliminar', command=self.eliminar_datos)
        self.btn_eliminar.config(width=20, font=(
            'Arial', 12, 'bold'), fg='#DAD5D6', bg='#BD152E', cursor='hand2', activebackground='#E15370')
        self.btn_eliminar.grid(row=5, column=2, padx=10, pady=10)

    def editar_datos(self):
        try:
            self.id_pelicula = self.tabla.item(self.tabla.selection())['text']

            self.nombre_pelicula = self.tabla.item(
                self.tabla.selection())['values'][0]
            self.duracion_pelicula = self.tabla.item(
                self.tabla.selection())['values'][1]
            self.genero_pelicula = self.tabla.item(
                self.tabla.selection())['values'][2]

            self.habilitar_campos()

            self.entry_nombre.insert(0, self.nombre_pelicula)
            self.entry_duracion.insert(0, self.duracion_pelicula)
            self.entry_genero.insert(0, self.genero_pelicula)

        except:
            titulo = 'Edición de datos'
            mensaje = 'No ha seleccionado ningun registro'
            messagebox.showerror(titulo, mensaje)

    def eliminar_datos(self):
        try:
            self.id_pelicula = self.tabla.item(self.tabla.selection())['text']

            # Ejecución del sql en la tabla
            eliminar(self.id_pelicula)

            # Mensaje de confirmación de registro eliminado
            # titulo = 'Elimminar un registro'
            # mensaje = 'El Registro fue eliminado Correctamente'
            # messagebox.showinfo(titulo, mensaje)

            # Recarga de la tabla para que se actualicen los datos en la vista
            self.tabla_peliculas()

            # Limopiamos todo el formulario y reiniciamos el id para que la próxima vez se ejecute correctamente
            self.id_pelicula = None

        except:
            titulo = 'Elimminar un registro'
            mensaje = 'No ha seleccionado ningún registro'
            messagebox.showerror(titulo, mensaje)
