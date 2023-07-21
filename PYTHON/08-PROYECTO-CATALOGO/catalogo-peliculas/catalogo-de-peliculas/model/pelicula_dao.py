from .conexion_db import ConnectDB
from tkinter import messagebox


def crear_tabla():
    conexion = ConnectDB()

    sql = '''
    CREATE TABLE peliculas(
        id_pelicula INTEGER,
        nombre VARCHAR(50),
        duracion VARCHAR(10),
        genero VAECHAR(20),
        PRIMARY KEY(id_pelicula AUTOINCREMENT)
    )
    '''
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
        titulo = 'Crear Registro'
        mensaje = 'La Tabla fue Creada Correctamente'
        messagebox.showinfo(titulo, mensaje)
    except:
        titulo = 'Crear Registro'
        mensaje = 'WARNING \nLa Tabla ya Existe'
        messagebox.showwarning(titulo, mensaje)


def borrar_tabla():
    conexion = ConnectDB()

    sql = 'DROP TABLE peliculas'
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
        titulo = 'Borrar Registro'
        mensaje = ' \nLa Tabla fue borrada con Éxito'
        messagebox.showinfo(titulo, mensaje)
    except:
        titulo = 'Borrar Registro'
        mensaje = 'ERROR: \nLa Tabla NO existe'
        messagebox.showerror(titulo, mensaje)


class Pelicula:
    def __init__(self, nombre, duracion, genero):
        self.id_pelicula = None
        self.nombre = nombre
        self.duracion = duracion
        self.genero = genero

    def __str__(self):
        return f'Pelicula[{self.nombre}, {self.duracion}, {self.genero}]'


def guardar(pelicula):
    conexion = ConnectDB()

    sql = f"""INSERT INTO peliculas (nombre, duracion, genero) VALUES ('{pelicula.nombre}', '{pelicula.duracion}', '{pelicula.genero}')
"""
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
        titulo = ' Guardar '
        mensaje = 'Registro Creado Exitosamente'
        messagebox.showinfo(titulo, mensaje)
    except:
        titulo = ' Conexión al Registro '
        mensaje = 'La tabla Películas NO ha sido Creada Previamente'
        messagebox.showerror(titulo, mensaje)


def listar():
    conexion = ConnectDB()

    lista_peliculas = []
    sql = 'SELECT * FROM peliculas'

    try:
        conexion.cursor.execute(sql)
        lista_peliculas = conexion.cursor.fetchall()
        conexion.cerrar()
    except:
        titulo = ' Conexión al Registro '
        mensaje = 'Para empezar, crea la tabla en la base de datos'
        messagebox.showwarning(titulo, mensaje)

    return lista_peliculas


def editar(pelicula, id_pelicula):
    conexion = ConnectDB()

    sql = f"""UPDATE peliculas
    SET nombre = '{pelicula.nombre}', duracion = '{pelicula.duracion}',
    genero = '{pelicula.genero}'
    WHERE id_pelicula = {id_pelicula}"""

    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()

    except:
        titulo = 'Edición de datos'
        mensaje = 'No se apodido editar este registro'
        messagebox.showerror(titulo, mensaje)


def eliminar(id_pelicula):
    conexion = ConnectDB()

    sql = f'DELETE FROM peliculas WHERE id_pelicula = {id_pelicula}'

    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except:
        titulo = 'Eliminar Datos'
        mensaje = 'No se pudo eliminar el registro'
        messagebox.showerror(titulo, mensaje)
