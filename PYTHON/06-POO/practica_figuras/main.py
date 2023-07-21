from figuras import Rectangulo, Circulo, probar_figura

def main():
    while True:
        menu = """

        <<<<<<  ÁREA Y PERÍMETRO DE FIGURAS GEOMÉTRICAS  >>>>>>

                1 - Rectángulo

                2 - Circulo

                3 - Salir de la aplicación

        Ingrese una opción:
        """

        opcion = input(menu)

        if opcion == '1':
                base = float(input("Ingrese la base del rectángulo: "))
                altura = float(input("Ingrese la altura del rectángulo: "))
                r = Rectangulo(base, altura)
                probar_figura(r)

        elif opcion == '2':
                radio = float(input("Ingrese el radio del círculo: "))
                c = Circulo(radio)
                probar_figura(c)

        elif opcion == '3':
            print('Cerrando Sistema')
            break

        else:
                print("Opción inválida. Intente nuevamente.")


# Punto de entrada de la aplicación
if __name__ == '__main__':
    main()


