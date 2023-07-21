/*
PROBLEMA:
Enunciado: Hallar el Cociente y el Residuo (reto) de dos números enteros

Análisis:
Para la solución de este problema, se requiere que el ususario ingrese dos números enteros y el sisitema realice el cálculo respectivo para hallar el cociente y el resideo, para esto, use la siguiente expresión:

Expresión algorítmica:
c <- n1 / n2
r <- n1 Mod n2

Entrada:
Dos números ( n1 y n2).

Salida:
. El Cociente (c)
.El Residuo (r)

DIAGRAMAS DE FLUJO

INICIO
|
n1,n2,c,r : Entero
|
Leer n1,n2
|
c <- n1 / n2
r <- n1 Mod n2
|
Escribir c,r
| Fin

PSEUDOCÓDIGO:

Inicio:
.Variables:
n1,n2,c,r : Entero

Entrada:
Leer n1, n2

.Proceso:
c <- n1 / n2
r <- n1 Mod n2

.Salida:
Escribir c, r

.Fin
*/



// Definir las variables que vamos a necesitar:
let n1,n2,c,r;

// Entrada de datos
n1 = parseInt(prompt('Ingrese un número Entero'));
n2 = parseInt(prompt('Ingrese un número Entero'));


// Proceso:
c = n1 / n2;
r = n1 % n2;


// Salida de datos
document.write('El cociente es ',c);
document.write('<hr>El residuo es ',r);






















