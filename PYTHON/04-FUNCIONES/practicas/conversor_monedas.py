'''
PRÁCTICA 04: CONVERSOR DE MONEDAS

* Crea un sistema que convierta moneda nacional a dolares,
por ejemplo de soles peruanos a dólares, pesos mexicanos a dólares, pesos colombianos a dólares.
* Para solucionar este problema se requiere que el ususario ingrese la cantidad de
monedas nacionales y luego realizar la conversión.
* Para este sistema debe haber un menú de navegación para seleccionar el tipo de moneda que hará
la conversión y también para cerrar el programa, el sistema no debe cerrarse si no lo desea
'''
def convertir(valor_dolar, pais):
    cantidad_moneda = float(input(f'Ingrese la cantidad de dinero de {pais}: '))

    dolares = cantidad_moneda / valor_dolar
    dolares = round(dolares, 2)
    print(f'${cantidad_moneda} es equivalente a ${dolares} Dólares')

def main():
    opcion = 0

    while opcion != 4:
        print("\n\n\n\n\n--------------- MENÚ DE CONVERSIÓN ---------------\n")
        print("1. Convertir Soles Peruanos a Dólares\n")
        print("2. Convertir Pesos Mexicanos a Dólares\n")
        print("3. Convertir Pesos Colombianos a Dólares\n")
        print("4. Salir\n")

        opcion = int(input("\nIngrese una opción: "))

        if opcion == 1:
            convertir(3.61, 'Soles Peruanos')
        elif opcion == 2:
            convertir(19.83, 'Pesos Mexicanos')
        elif opcion == 3:
            convertir(3573.47, 'Pesos Colombianos')
        elif opcion == 4:
            print("\nSaliendo del programa...")
        else:
            print("\nOpción inválida. Por favor, ingrese una opción válida.")

if __name__ == '__main__':
    main()
