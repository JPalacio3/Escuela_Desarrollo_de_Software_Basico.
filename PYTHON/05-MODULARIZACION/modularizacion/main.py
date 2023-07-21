# Importamos el módulo fibonacci para usar sus funciones

# import fibonacci
# fibonacci.fibo(1000)
# print(fibonacci.fibo2(1000))

# from fibonacci import fibo, fibo2
# fibo(1000)
# print(fibo2(1000))

# from fibonacci import *
# fibo(1000)
# print(fibo2(1000))

import fibonacci as f
from fibonacci import fibo2 as f2
f.fibo(1000)
print(f2(1000))
