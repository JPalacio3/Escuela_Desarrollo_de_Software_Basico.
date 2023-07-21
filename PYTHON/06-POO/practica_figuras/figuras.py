import math as m

class Figura(object):
    def __init__(self,nombre):
        self.nombre = nombre

    def area(self):
        pass

    def perimetro(self):
        pass



class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.nombre = __class__.__name__
        self.base = base
        self.altura = altura

    def area(self):
        return round(self.base * self.altura, 2)

    def perimetro(self):
        return round(2 * self.base + 2 * self.altura, 2)

    def __str__(self):
        return f'\n{self.nombre}\n[base: {self.base} \nAltura: {self.altura}]'



class Circulo(Figura):
    def __init__(self, radio):
        self.nombre = __class__.__name__
        self.radio = radio

    def area(self):
        return round(m.pi * self.radio**2, 2)

    def perimetro(self):
        return round(2* m.pi * self.radio, 2)

    def __str__(self):
        return f'\n{self.nombre}\n[Radio: {self.radio} ]'



def probar_figura(figura):
    print(figura)
    print('Area: ', figura.area())
    print('Perímetro: ', figura.perimetro())
