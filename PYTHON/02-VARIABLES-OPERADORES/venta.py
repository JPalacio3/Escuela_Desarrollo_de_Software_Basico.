'''
Práctica 02:

Enunciado: Dado el valor de la venta de un producto, hallar el IGV (18%) y el precio de venta.

Análisis:
Para la solución de este problema, se requiere que el usuario ingrese el valor de la venta del prodcuto
y el sistema realice el cálculo respectivo para hallar el IGV y el precio de venta, para esto use la siguiente expresión:

igv = vv * 0.18
pv = vv + igv
'''

# Ingreso de datos
print('Ingrese el valor de la venta a continuación: ')

vv = input('Valor de la Venta: $ ')
vv = float(vv)

# Cálculo de la operación
igv = round(vv * 0.18,2)
pv = round(vv + igv,2)

# Salida de datos
resultado = f'El Valor de la venta ingresado es de:   $ {vv} \nEl valor del IGV para esta venta es de: $ {igv}\nY el valor Total de la Venta es de:     $ {pv}'

print('='*50)
print('-'*15, 'FACTURA DE VENTA' ,'-'*15)
print(resultado)
print('='*50)
