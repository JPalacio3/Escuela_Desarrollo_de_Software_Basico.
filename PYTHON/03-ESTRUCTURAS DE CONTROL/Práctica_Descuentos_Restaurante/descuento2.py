'''
PRÁCTICA:

Enunciado:
Debido a los ecelentes resultados, el restaurante decide ampliar sus ofertas de acuerdo a la siguiente escala de consumo.
Determinar el monto del descuento, el importe del descuento, y el monto a pagar:

hasta $100 -> 10
mayor a $100 -> 20
mayor a 200 -> 30

Análisis:
Para la solución de este problema, se requiere que el usuario ingrese el monto del consumo y el sistema verifica y
calcula el monto del descuento y el importe a pagar.

* monto del usuario
* impuesto
* Importe a pagar
'''

# Definción de las variables
consumo = int(input('Ingrese a continuación el monto del consumo: '))
igv = consumo * 0.19
total = consumo + igv
descuento1 = total * 0.10
descuento2 = total * 0.20
descuento3 = total * 0.30


# Salida de datos

if consumo > 0:

    if consumo <= 100:
        # Descuento del 10%
        print('\n')
        print('='*20, 'FACTURA DE VENTA', '='*20)
        print('\n')
        print('El Consumo registrado es de : $', consumo)
        print('El descuento que aplica es del 10%')
        print('El monto del descuento que aplica es de: $', round(descuento1, 2))
        print('El IGV aplicado para esta venta es de: $', round(igv, 2))
        print('El importe a pagar es de $', round(total - descuento1, 2))
        print('\n')
        print('='*57)

    elif consumo > 100 and consumo < 200:
        # Descuento del 20%
        print('\n')
        print('='*20, 'FACTURA DE VENTA', '='*20)
        print('\n')
        print('El Consumo registrado es de : $', consumo)
        print('El descuento que aplica es del 20%')
        print('El monto del descuento que aplica es de: $', round(descuento2, 2))
        print('El IGV aplicado para esta venta es de: $', round(igv, 2))
        print('El importe a pagar es de $', round(total - descuento2, 2))
        print('\n')
        print('='*57)

    else:
        print('\n')
        print('='*20, 'FACTURA DE VENTA', '='*20)
        print('\n')
        print('El Consumo registrado es de : $', consumo)
        print('El descuento que aplica es del 30%')
        print('El monto del descuento que aplica es de: $', round(descuento3, 2))
        print('El IGV aplicado para esta venta es de: $', round(igv, 2))
        print('El importe a pagar es de $', round(total - descuento3, 2))
        print('\n')
        print('='*57)

else:
    print('error -> HA INGRESADO UNA CANTIDAD INVÁLIDA')

'''
Ingrese a continuación el monto del consumo: 300


==================== FACTURA DE VENTA ====================


El Consumo registrado es de : $ 300
El descuento que aplica es del 30%
El monto del descuento que aplica es de: $ 107.1
El IGV aplicado para esta venta es de: $ 57.0
El importe a pagar es de $ 249.9


=========================================================
'''
