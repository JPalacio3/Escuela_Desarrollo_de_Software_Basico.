# PRÁCTICA 05: JURGO ADIVINA EL NÚMERO
'''
* Consiste un pedirle al ususario que ingrese un número entre 1 y 100 y el sistema debe validar
que el número ingresado por el ususario el el número random que previamente eligió el sistema.

* Debe contar con un número definido de vidas para lograrlo e irse restando una cada vez que se equivoque.
* Debe tener una pista en caso de que el número ingresado sea mayor o menor.
* Mostrar un mensaje cuando pierda todas las vidas o cuando logre adivinar el número.
* Debe tener la capacidad de elegir entre modo fácil, medio y difícil, y tener una opción para salir del juego

'''


import random

def jugar(vidas):
    numero_random = random.randint(1,100)
    numero_elegido = None

    while numero_random != numero_elegido:
        numero_elegido = int(input('\nIngrese un número entre 1 y 100: '))

        if numero_random < numero_elegido:
            print('Elige un número más pequeño')
            vidas -=1
        elif numero_random > numero_elegido:
            print('Elige un número más grande')
            vidas -= 1
        if vidas == 0:
            print(f'\n\n            GAME OVER')
            break

        print(f'Te quedan {vidas} vidas !!')

    if numero_elegido == numero_random:
        print(f'\n\n                GANASTE !!!!!')

def main():
    while True:
        menu = """
        --------------  ADIVINA EL NÚMERO ALEATORIO -----------------

                    1 - NIVEL FÁCIL
                    2 - NIVEL INTERMEDIO
                    3 - NIVEL DIFÍCIL
                    4 - Salir del Juego

        INGRESE UNA OPCIÓN: """

        opcion = input(menu)

        if opcion == '1':
            jugar(10)
        elif opcion == '2':
            jugar(6)
        elif opcion == '3':
            jugar(5)
        elif opcion == '4':
            print(f'\n                   SALIENDO DEL JUEGO')
            break
        else:
            print(f'\nEsa es una opción Opción Inválida Campeón, Selecciona un nivel válido\n')



if __name__ == '__main__':
    main()
