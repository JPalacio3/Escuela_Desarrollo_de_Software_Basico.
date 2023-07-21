'''
PRÁCTICA 02: PRIMALIDAD

*Crear  un sistema que detecte si un número es primo o no.
* Para solucionar este problerma se requiere que el usuario ingrese un número por teclado
y el sistema detecte si es primo o no
* Un número primo es aquel que se puede dividir únicamente solo dos veces por 1 y por sí mismo.
'''
def es_primo(numero):
    contador = 0

    for i in range(1, numero + 1):
        if i == 1 or i == numero:
            continue

        # Verifica que la división con los números hasta el número ingresado sea igual a 0
        if numero % i == 0:
            contador += 1

    if contador == 0:
        return True
    else:
        return False


def main():
    numero = int(input('Ingrese un número entero: '))

    if es_primo(numero):
        print(f'{numero} -> ES UN NÚMERO PRIMO')
    else:
        print(f'{numero} -> NO es un número primo')

if __name__ == '__main__':
    main()


# Ingrese un número entero: 5
# 5 ES UN NÚMERO PRIMO
