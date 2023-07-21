'''
PRÁCTICA:

Enunciado:
Un restaurante ofrece un descuento del 10% para consumo de hasta $ 100, y un descuento del 20% para consumos mayores.
Para ambos casos se aplica un impuesto del 19%.
Determinar el monto del descuento, el impuesto y el importe a pagar.

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
descuento10 = total * 0.10
descuento20 = total * 0.20
encabezado = print(f'='*15, 'TICKET DE PAGO', '='*15)


# Salida de datos
if consumo >= 100:
    # Descuento del 10%
    encabezado, '\n'
    print(f'Consumo Registrado es de $', consumo, '\nDescuento es de 10%',
          '( $', descuento10, ').', '\nPAGO TOTAL ES DE: $', total - descuento10)
    print(f'#'*50)
else:
    # Descuento del 20%
    encabezado, '\n'
    print(f'El consumo registrado es de $', consumo, '\nDescuento es de 20%',
          '( $', descuento20, ').', '\nPAGO TOTAL ES DE: $', total - descuento20)
    print(f'#'*50)


'''
Ingrese a continuación el monto del consumo: 100

========== TICKET DE PAGO ==========
Consumo Registrado es de $ 100
Descuento es de 10% ( $ 11.9 ).
PAGO TOTAL ES DE: $ 107.1
####################################

'''
