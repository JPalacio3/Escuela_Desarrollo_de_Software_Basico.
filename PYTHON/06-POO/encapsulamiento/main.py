from persona import Persona

persona1 = Persona('Joel', 33)
print(persona1.get_nombre())
persona1.set_nombre('Alberto')
print(persona1.get_nombre())

'''
# Salida:
λ main.py

Joel
Alberto
'''
