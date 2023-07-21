# El concepto de Polimorfismo en Python indica que, se pueden
# reescribir los métodos de la clase padre, conservando el mismo
# pero cambiando su funcionalidad según sea necesario en diferentes
# objetos.

class Persona(object):
    def __init__(self, nombre):
        self.nombre = nombre

    def moverse(self):
        print('Ando caminando')


class Atleta(Persona):
    def moverse(self):
        print('Estoy corriendo')


class Ciclista(Persona):
    def moverse(self):
        print('Estoy moviéndome en bicicleta')



# Herencia MÚLTIPLE: Permite que una clase hija herede los métodos de varias clases padre

class A:
    def __init__(self):
        print('Soy la clase A')
    def a(self):
        print('Soy método de A')


class B:
    def __init__(self):
        print('Soy la clase B')
    def b(self):
        print('Soy método de B')

# CLASE CON MULTIHERENCIA
class C(A,B):
    def c(self):
        print('Soy método de C')


c1 = C() # Soy la clase A
# c1.a() # Soy método de A
# c1.b() # Soy método de B
