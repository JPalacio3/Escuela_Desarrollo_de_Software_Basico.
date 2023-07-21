numeros = {
    'uno': 1,
    'dos': 2,
    'tres': 3,
    'cuatro': 4,
    'cinco': 5
}

# Conocer el tipo de dato
tipo = type(numeros)

# Acceder s los elementos por medio de su clave
uno = numeros['uno']
tres = numeros['tres']

# Agregar un elemento
numeros['seis'] = 6

# Buscar un elemento, por medio de su clave, y devuelve su valor
buscar = numeros.get('cuatro', 'NO SE ENCONTRÓ')

# Imprimir todas las claves de un diccionario
claves = numeros.keys()

# Imprimir todos los valores del diccionario
valores = numeros.values()

# Devolver una lista con clave y valor
lista = numeros.items()

# Eliminar un elemento indicando la clave
eliminar = numeros.pop('seis', 'ESTE ELEMENTO NO EXISTE')

# Iterar en la lista
for numero in numeros:
    print(numero)

# Iterar en los valores de la lista
for numero in numeros.values():
    print(numero)

# Iterar en la lista con clave y valor
for clave, valor in numeros.items():
    print(clave, valor)


# Eliminar todos los elementos
# numeros.clear()

print(numeros)
print(tipo)
print(uno)
print(tres)
print(buscar)
print(claves)
print(valores)
print(lista)
print(eliminar)
