import mi_paquete.aritmetica as a

def main():
    suma = a.sumar(4,5,6,5,5,5)
    resta = a.resta(10,6)
    potencia = a.potencia(3,3)

    print('La suma es: ', suma)
    print(' La resta es: ', resta)
    print('La potencia es: ', potencia)

if __name__ == '__main__':
    main()
