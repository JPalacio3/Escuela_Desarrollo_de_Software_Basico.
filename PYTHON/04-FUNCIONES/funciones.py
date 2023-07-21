
def saludar():
	global nombre
	nombre = 'Joel Palacio'
	print('Hola', nombre ,'desde la función saludar')
	return 'Hola Mundo desde la función saludar' # Retonra un valor e indica el término de la función



valor = saludar() # Llamada de la función para que se ejecute
print(valor)
print('Hola', nombre ,'Desde fuera de la función saludar, asignando el nombre de la variable "nombre" de manera global')


def saludo():
	nombre = 'JOEL'
	edad = 33
	return f'Hola {nombre}, tienes {edad} años de edad.'

saludo = saludo()
print(saludo)
