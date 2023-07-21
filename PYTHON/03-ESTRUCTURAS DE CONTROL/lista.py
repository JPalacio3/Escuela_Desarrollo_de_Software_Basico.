datos = ['Joel', 'Alberto', 33]

# Agrega el elemento al final de la lista
datos.append('Palacio')

# Permite extender la lista
datos.extend(datos)

# Permite insertar un elemento en la posición que le indiquemos según el índice
datos.insert(1, 100)

# Se puede redefinir la lista simplemete nombrándola y asignando
datos = ['Joel', 'Alberto', 'Palacio', 33]

# Se remueve un elemento de la lista
datos.remove('Palacio')


# Conocer la posición de un elemento de la lista
datos.index(33)

# Conocer cuántas veces se repite un elemento dentro de la lista
datos = [100, 100, 25, 'Colombia']
datos.count(100)

# Eliminar el último elemento de la lista
datos.pop()

# Eliminar todo slos elememtos de la lista
datos.clear()

print(datos)

#######################################################

frutas = ['manzana', 'pera', 'naranja', 'uva', 'fresa']

# Ordenar alfabeticamente los objetos de la lista
frutas.sort()

# Invertir la lista
frutas.reverse()

# Realizar una copia de la lista
frutas2 = frutas.copy()
print(frutas2)

print(frutas)
