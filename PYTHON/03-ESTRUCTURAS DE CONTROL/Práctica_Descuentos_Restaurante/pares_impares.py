'''
Práctica:
Guardar resultado de números pares e impares:
Crea dos listas y una tupla que tendrá números de 1 a 9.
La primera lista se llamará pares y la segunda impar, ambos estarán vacíos.
Después multiplica cada uno de los números de la tupla por un número aleatorio entre 1 y 100.
Si el resultado es par se guarda en la lista de pares y si es impar se guarda en la lista de impares.

Muestra por consola: -la multiplicación que se produce junto con su resultado que con el formato 2 x 3 = 6 y
la lista de pares e impares.
'''
import random

# Variables
pares = []
impares = []
operador = (1, 2, 3, 4, 5, 6, 7, 8, 9)  # Tupla para los operadores

# Operación
for n in operador:
    numero_random = random.randint(1, 100)
    resultado = n * numero_random

    if resultado % 2 == 0:
        print(f'{n} x {numero_random} = {resultado}')
        pares.append(resultado)
    else:
        print(f'{n} x {numero_random} = {resultado}')
        impares.append(resultado)

print('\nLista de Pares:', pares)
print('Lista de Impares:', impares)
