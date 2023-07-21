class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def detalle_persona(self):
        print(f'Nombre: {self.nombre} \nEdad: {self.edad}')

    def __str__(self):
        return f'Nombre: {self.nombre} \nEdad: {self.edad}'


class Cliente(Persona):
    pass



# Clase empleado que hereda de Persona:
'''
La función super() en Python se utiliza para llamar y acceder a los métodos y atributos
de la clase base desde una clase derivada. Permite extender o
modificar el comportamiento de la clase base sin tener que volver a escribir todo el código.
'''

class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)
        self.sueldo = sueldo

    def detalle_empleado(self):
        super().detalle_persona()
        print('sueldo: ', self.sueldo)

    def __str__(self):
        return super().__str__() + f'\nSueldo: {self.sueldo}'



# Clase Trabajador hereda de la clase padre Persona pero sin usar la función super()
'''
Cuando una clase hereda de otra, se convierte en una subclase de la clase base
(también conocida como superclase o clase padre), y la clase base se convierte
en la clase padre de la subclase. La subclase hereda todos los atributos y métodos
de la clase base, y puede agregar nuevos atributos y métodos o modificar los existentes.
En Python, puedes crear una subclase sin utilizar el método super().
En su lugar, puedes llamar directamente al método __init__() de la clase base
y pasarle los argumentos necesarios.
'''

class Trabajador(Persona):
    def __init__(self, nombre, edad, sueldo):
        Persona.__init__(self, nombre, edad)
        self.sueldo = sueldo

    def detalle_trabajador(self):
        Persona.detalle_persona(self)
        print(f'Sueldo: {self.sueldo}')

    def __str__(self):
        return Persona.__str__(self) + f'\nSueldo: {self.sueldo}'
