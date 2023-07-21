import sys

if len(sys.argv) == 3:
    texto = sys.argv[1]
    cantidad = int(sys.argv[2])

    c = 0
    while c < cantidad:
        print(texto)
        c+=1
else:
    print('Hay un error, ingrese los argumentos correctamente')
    print('\nEj: \nentrada_script.py "Hola mundo" 5')


# entrada_script.py "Hola mundo" 5
# Hola mundo
# Hola mundo
# Hola mundo
# Hola mundo
# Hola mundo

# Error:
# entrada_script.py "Hola mundo"
# Hay un error, ingrese los argumentos correctamente

# Ej:
# entrada_script.py "Hola mundo" 5
