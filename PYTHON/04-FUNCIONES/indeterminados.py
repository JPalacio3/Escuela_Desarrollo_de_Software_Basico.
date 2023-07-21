
# Parámetros indeterminados por posición
def sumar(*args):
    suma = 0
    for n in args:
        suma += n
    return suma

sumaTotal = sumar(1,2,3,4,5,6,10,20,30)
print('La suma total es ', sumaTotal)
# La suma total es  81

###########################################################

# Parámetros indeterminados por nombre
def sumar(*args, **kwargs):
    suma = 0
    for n in args:
        suma += n
    return suma, kwargs

sumaTotal, datos= sumar(1,2,3,4,5,6,10,20,30, nombre='Joel', edad= 33)
print('La suma total es ', sumaTotal, '\nY los datos en el diccionario son:', datos)
# La suma total es  81
# Y los datos en el diccionario son: {'nombre': 'Joel', 'edad': 33}
