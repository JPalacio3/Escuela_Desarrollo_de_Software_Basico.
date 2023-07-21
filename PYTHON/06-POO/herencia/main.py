from persona import Cliente as c
from persona import Empleado as e
from persona import Trabajador as t

cliente1 = c('Joel', 33)
cliente2 = c('Alberto', 32)

cliente1.detalle_persona()
print(cliente2)

empleado1 = e('Joel', 33, 18000)
empleado2 = e('Alberto', 32, 20000)

empleado1.detalle_persona()
print(empleado2)


trabajador1 = t('Palacio', 33, 25000)
trabajador2 = t('Cano', 32, 30000)

trabajador1.detalle_trabajador()
print(trabajador2)
