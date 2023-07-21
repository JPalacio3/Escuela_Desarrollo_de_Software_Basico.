'''
Práctica01:
Calcular el conciente y residuo enunciado: Hallar el cociente y residuo (resto) de dos números enteros.
Análisis: Para la solución de este problema, se requiere que el usario ingrese dos nómeros enteros y el sistema realice el cálculo respectivo para hallar el cociente y residuo.
'''


print('Práctica de Cociente y Residuo de dos números. \nDebes Ingresar Dos números enteros:  ')

# Entrada de datos
a = input('Ingrese el Primer Número: ')
b = input('Ingrese el Segundo Número: ')

# Casting de datos para convertirlos en números antes de la operación
a = int(a)
b = int(b)

# Operación
cociente = a / b
residuo = a % b

# Imprimir en consola el resultado de la operación
resultado = f'Para los números ingresados, el resultado obtenido es: \nCociente: {cociente} \nResiduo: {residuo}'
print(resultado)
