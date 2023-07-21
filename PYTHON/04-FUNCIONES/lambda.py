

sumar = lambda a, b :  a+b
duplicar = lambda n : n*2
par = lambda n : n % 2 == 0
impar = lambda n : n % 2 != 0
revertir = lambda cadena : cadena[::-1]


print(sumar(2,3)) #5
print(duplicar(5)) #10
print(par(2)) # True
print(impar(2)) # False
print(revertir('hola')) #aloh

