c = 0
x = 0

# Se indica que c debe imprimirse sumando uno hasta llegar a 10
while c < 10:
    c += 1
    print(c)

# El bucle debe terminar una vez que c sea igual a 5 por medio de la instrucción break
    if c == 5:
        print('Termina el bucle')
        break

else:
    print('Fin de la instrucción')
'''
1
2
3
4
5
Termina el bucle
'''


# Se indica que x debe imprimirse sumando uno hasta llegar a 10
while x < 10:
    x += 1
    print(x)

# El bucle debe saltar a la siguiente iteración cuando x sea 5 por medio de la instrucción continue
    if x == 5:
        print('Salta a la siguiente Iteración')
        continue
    print('Después de continue')

else:
    print('Fin de la instrucción')

'''
1
Después de continue
2
Después de continue
3
Después de continue
4
Después de continue
5
Salta a la siguiente Iteración
6
Después de continue
7
Después de continue
8
Después de continue
9
Después de continue
10
Después de continue
Fin de la instrucción
'''
