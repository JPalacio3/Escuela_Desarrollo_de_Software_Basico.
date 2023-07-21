class Persona:

    # Los atributos Privados se definen con el signo __, ya que en el lenguaje no existe una palabra
    # reservada para tal fin.
    __nombre = None
    __Edad = None

    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad

    def __metodo_privado(self):
        print('Soy un método privado')

# Para poder acceder y/o modificar los atributos privados de la clase, debemos
# crear método públicos
    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_edad(self):
        return self.edad

    def set_edad(self, edad):
        self.edad = edad



    def __str__(self):
        return f'Nombre: {self.__nombre} \nEdad: {self.__edad}'
