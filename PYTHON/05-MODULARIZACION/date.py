from datetime import datetime as d

print(d.now()) # Devuelve la información del tiempo actual

dt = d.now()
print(dt.year) #Imprime año actual
print(dt.month) #Imprime mes actual
print(dt.day) #Imprime dia actual
print(dt.hour) #Imprime hora actual
print(dt.minute) #Imprime minuto actual
print(dt.second) #Imprime segundo actual
print(dt.microsecond) #Imprime microsegundo actual

'''
# Salidas:
λ date.py
2023-06-08 16:36:22.512553
2023
6
8
16
36
22
512553
'''
