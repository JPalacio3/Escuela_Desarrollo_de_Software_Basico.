from sys import argv


if len(argv) ==4:
    nombre = argv[1]
    edad = int(argv[2])
    altura = float(argv[3])

# Maneras de formatear:
    print(f'nombre: {nombre} \nEdad: {edad}\nAltura: {altura}')
    # print('nombre: {} \nEdad: {}\nAltura: {}'.format(nombre, edad, altura))
    # print('nombre: {n} \nEdad: {e}\nAltura: {a}'.format(a = altura, n = nombre,e = edad))
    #print('nombre: %s \nEdad: %i \nAltura: %f'%(nombre, edad, altura))



else:
    print('Hay un error, ingrese los argumentos correctamente')
    print('\nEj: \nformateo.py "Hola mundo" 5 1.78')
