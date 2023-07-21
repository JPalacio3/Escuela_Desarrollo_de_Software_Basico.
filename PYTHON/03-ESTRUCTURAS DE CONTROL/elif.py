# Detectar si una letra es una vocal o no

# Ingreso de datos
v = input(' Ingrese una letra: ')

# Operación
if v == 'a' or v == 'A':
    print(f'{v} ES UNA VOCAL')
elif v == 'e' or v == 'E':
    print(f'{v} ES UNA VOCAL')
elif v == 'i' or v == 'I':
    print(f'{v} ES UNA VOCAL')
elif v == 'o' or v == 'O':
    print(f'{v} ES UNA VOCAL')
elif v == 'u' or v == 'U':
    print(f'{v} ES UNA VOCAL')

else:
    print(f'{v} CORRESPONDE A UNA CONSONANTE')




# Forma más simplicada de hacer la misma operación:
# Lista de vocales
vocales = ['a', 'e', 'i', 'o', 'u']

# Ingreso de datos
v = input('Ingrese una letra: ')

# Operación
if v.lower() in vocales:
    print(f'{v} ES UNA VOCAL')
else:
    print(f'{v} CORRESPONDE A UNA CONSONANTE')
