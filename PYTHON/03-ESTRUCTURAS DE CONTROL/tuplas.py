# LAS TUPLAS SON INMUTABLES, Nno obstante, puedes realizar ciertas operaciones en ellas, como concatenación de tuplas, duplicación de tuplas y desempaquetado de tuplas.


tupla = ('Joel', 'Alberto', 33, True)

# No se pueden modificar pero se puede acceder a los elementos
el = tupla[0]
el = tupla[:2]

# err = tupla[0] = 'Colombia'
# Arroja un error ya que la tupla es inmutable, o sea, no se puede modificar

# Conocer la extensión de la tupla
len = len(tupla)

# Conocer el índice de un elemento
ind = tupla.index(33)


print(tupla)
print(el)
# print(err)
print(len)
print(ind)
