
'''
Práctica 01: PALÍNDROMO

* Crear un sistema que detecte si una palabra es palíndroma o no.
* Para solucionar este problema, el usuario debe ingresar por pantalla una palabra y el sistema verifica si es palpindromo o no
* Una palabra palíndroma se lee de igual forma como de la derecha y de la izquierda
'''

def palindromo (palabra):
    # Eliminar los espacios
    palabra = palabra.replace(' ', '')

    # Convertir todas las letras en minúsculas
    palabra = palabra.lower()

    palabra_invertida = palabra[::-1]

    # Verificar si es palíndroma o no
    if palabra == palabra_invertida:
        return True
    else:
        return False

# Función Principal
def main():
    palabra = input('Ingrese una frase o palabra: ')
    es_palindromo = palindromo(palabra)

    if es_palindromo:
        print(f'{palabra} es Palíndromo')
    else:
        print(f'{palabra} NO es palíndromo')

# Punto de entrada de la aplicación
if __name__ == '__main__':
    main()
