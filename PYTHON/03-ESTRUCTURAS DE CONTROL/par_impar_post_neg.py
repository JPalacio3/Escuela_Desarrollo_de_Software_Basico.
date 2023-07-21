
# Condición anidada para calcular, además de si un número es par o impar, y si es positivo o negativo

# Ingreso de datos
n = int(input('Ingrese un Número a continuación: '))

# Realizar la operación
if n != 0:
    if n > 0:
        if n % 2 == 0:
            print(f'El número {n} es PAR POSITIVO')
        else:
            print(f'El número {n} es IMPAR POSITIVO')
    else:
        if n % 2 == 0:
            print(f'El número {n} es PAR NEGAITVO')
        else:
            print(f'El número {n} es IMPAR NEGATIVO')
else:
    print(f'El número {n} es Neutro')
