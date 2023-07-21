# Módulo que se utilizará para generar la secuencia de Fibonacci :
# El número de Fibonacci es una secuencia matemática infinita en la que cada número
# se obtiene sumando los dos números anteriores. Los primeros dos números de la
# secuencia de Fibonacci son 0 y 1. A partir de ahí, cada número se calcula sumando
# los dos números anteriores. La secuencia comienza de la siguiente manera:

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...


def fibo(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print('\n')


def fibo2(n):
    resultado = []
    a, b = 0, 1
    while a < n:
        resultado.append(a)
        a, b = b, a + b

    return resultado
