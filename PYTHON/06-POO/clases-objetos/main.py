from persona import Persona as p

# CREACIÓN DE LOS OBJETOS SIN CONSTRUCTOR

# persona1 = p()
# persona2 = p()
# persona3 = p()
# persona4 = p()

# persona1.nombre = 'Joel'
# persona1.edad = 33
# persona2.nombre = 'Alberto'
# persona2.edad = 32
# persona3.nombre = 'Palacio'
# persona3.edad = 31
# persona4.nombre = 'Cano'
# persona4.edad = 30

# print('=' *25)
# persona1.mostrar_datos()
# print('=' *25)

# persona2.mostrar_datos()
# print('=' *25)

# persona3.mostrar_datos()
# print('=' *25)

# persona4.mostrar_datos()
# print('=' *25)

# '''
# # Salida

# λ main.py

# =========================
# Nombre: Joel
# Edad: 33
# =========================
# Nombre: Alberto
# Edad: 32
# =========================
# Nombre: Palacio
# Edad: 31
# =========================
# Nombre: Cano
# Edad: 30
# =========================

# '''



#  CREACIÓN DE LOS OBJETOS UTILIZANDO UN CONSTRUCTOR __init__ DENTRO DE LA CLASE
print('=' *25)
persona1 = p('Joel', 33)
persona1.mostrar_datos()
print('=' *25)
persona2 = p('Alberto', 32)
persona1.mostrar_datos()
print('=' *25)
persona3 = p('Palacio', 31)
persona1.mostrar_datos()
print('=' *25)
persona4 = p('Cano', 30)
persona1.mostrar_datos()
print('=' *25)


'''
# Salidas:

λ main.py
=========================
Nombre: Joel
Edad: 33
=========================
Nombre: Joel
Edad: 33
=========================
Nombre: Joel
Edad: 33
=========================
Nombre: Joel
Edad: 33
=========================

'''
