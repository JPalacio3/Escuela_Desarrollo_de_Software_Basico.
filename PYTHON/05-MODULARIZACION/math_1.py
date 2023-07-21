import math as m

print(m.pi) #Imprimir  la constante Pi
print(m.e) # Impeimw la constante Euler
print(m.floor(4.99)) #Redondear hacia abajo
print(m.ceil(4.001)) #Redondear hacia arriba

n = [0.955, 1,2,3]
print(m.fsum(n)) #Suma todos los elementos dentro de la lista

print(m.trunc(45.7545)) #Trunca el valor (ignora los valores después del punto decimal)

print(m.pow(2, 3)) #Eleva el primer número del parámetro a la potencia del segundo parámetro

print(m.sqrt(16)) #Calculo de la raíz cuadrada

'''
# Salidas:
λ  math_1.py
3.141592653589793
2.718281828459045
4
5
6.955
45
8.0
4.0
'''
