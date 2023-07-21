def factorial(n):
    print('Valor Inicial => ', n)
    if n > 1:
        n = n * factorial(n-1)
    print('Valor Final ', n)
    return n

n = int(input('Ingrese un número entero a continuación: '))
f = factorial(n)

print(f'El factorial de {n} es :', f)
# salida:
#Ingrese un número entero a continuación: 5
# Valor Inicial =>  5
#Valor Inicial =>  4
#Valor Inicial =>  3
#Valor Inicial =>  2
#Valor Inicial =>  1
#Valor Final  1
#Valor Final  2
#Valor Final  6
#Valor Final  24
#Valor Final  120
#El factorial de 5 es : 120

