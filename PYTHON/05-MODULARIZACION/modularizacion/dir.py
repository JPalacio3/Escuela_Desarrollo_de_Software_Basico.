# La función dir() se utiliza para extraer toda la información en un módulo en específico

import fibonacci
import sys
import builtins

print('fibonacci: \n',dir(fibonacci))
print('sys: \n',dir(sys))
print('*: \n',dir())
print('builtins: \n',dir(builtins))
