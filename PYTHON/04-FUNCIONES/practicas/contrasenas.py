'''
PRÁCTICA 03: GENERADOR DE CONTRASEÑAS

* Crea un sistema que genere una contraseña aleatoria.
* Para solucionar este problema se requiere listas, listas mayúsculas,
lista de minúsculas, lista de números y lista de símbolos;
y luego armar una contraseña aleatoria sacando carácteres de estas listas.

'''

import random

def generar_contrasena():
    mayusculas = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    minusculas = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    simbolos = ['#', '$', '%', '/', '¿', '?', '!', '&']
    numeros = ['1','2','3','4','5','6','7','8','9','0']

    caracteres = mayusculas + minusculas + simbolos + numeros
    contrasena = []

    for i in range(15):
        caracter_random = random.choice(caracteres)
        contrasena.append(caracter_random)

    contrasena = "".join(contrasena)
    return contrasena


def main():
    contrasena = generar_contrasena()
    print(f'Tu nueva Contraseña es: {contrasena}')

if __name__ == '__main__':
    main()
