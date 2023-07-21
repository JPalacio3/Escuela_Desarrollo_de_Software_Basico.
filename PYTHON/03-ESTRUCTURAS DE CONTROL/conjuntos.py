mi_conjunto = {1, 2, 3}

# Agregar elementos al conjunto

mi_conjunto.add(4)
print(mi_conjunto)  # Output: {1, 2, 3, 4}

# Eliminar elementos del conjunto
mi_conjunto.remove(2)
print(mi_conjunto)  # Output: {1, 3, 4}

conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}

# Unión de conjuntos
union = conjunto1.union(conjunto2)
print(union)  # Output: {1, 2, 3, 4, 5}

# Intersección de conjuntos
interseccion = conjunto1.intersection(conjunto2)
print(interseccion)  # Output: {3}

# Diferencia de conjuntos
diferencia = conjunto1.difference(conjunto2)
print(diferencia)  # Output: {1, 2}
