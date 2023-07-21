# Parámetros : Variables que se definen dentro de los paréntesis de las funciones
# Argumentos: Los valores que se asignan a los argumentos al momento de la ejecución
####################################################################################
def saludar(nombre) :

    edad = 33
    return f'Hola {nombre} desde la función Saludar'

saludo = saludar('Joel')

print(saludo)

####################################################################################
def sumar(a=0,b=0) :
    return a + b

suma = sumar(4,5)
print(f'la suma es {suma}')

######################################################################################
def restar(a=None,b=None) :
    if a == None or b == None:
        print('No hay valores asignados para restar')
        return

    return a-b
    print(f'La resta es {resta}')

resta = restar(3)

######################################################################################
