# EL PRIMER ELEMENTO EN ENTRAR ES EL PRIMERO EN SALIR

from collections import deque

cola = deque(['Alberto', 'Palacio', 33, 'Colombia'])

# Agregar un elemento en la cola
cola.append('Joel')

# Eliminar el primer elemento de la cola
cola.popleft()


print(cola)
