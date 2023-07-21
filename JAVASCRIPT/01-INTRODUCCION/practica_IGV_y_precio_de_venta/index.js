/*
PROBLEMA:

ENUNCIADO:
Dado el valor de la venta de un producto, hallar el IGV(19%) y el precio de Venta.

ANÁLISIS:
Para la solución de este problema, se requiere que el ususario ingrese el valor de la venta del producto y el sistema realice el cálculo respectivo para hallar el IGV y el precio de venta, para esto use la siguiente expresión:

EXPRESIÓN ALGORÍTMICA:
igv <- vv * 0.19
pv <- vv + igv

ENTRADA:
Valor de Venta(vv)

SALIDA:
. El IGV (igv)
. Precio de Venta (pv)


DIAGRAMA DE FLUJO

INICIO
|
vv,igv,pv : Real
|
Leer vv
|
igv = vv*0.19
pv = vv+igv
|
Escribir igv, pv
|
FIN

PSEUDOCÓDIGO:

Inicio
. Variables:
vv, igv, pv : Real

.Entrada
Leer vv

.Proceso
igv = vv*0.19
pv = vv+igv

.Salida
Escribir igv, pv

FIN
*/




// DEFINICIÓN DE LAS VARIABLES
let vv = 0,igv = 0,pv = 0;

// ENTRADA DE DATOS
vv = Number(prompt('Ingrese Valor de Venta'));

// PROCESO
igv = vv * 0.19;
pv = vv + igv;

// SALIDA DE DATOS
document.write(`<hr> <h2> El valor de la venta es:            $ ${vv} </h2>`);
document.write(`<hr> <h2> El valor del IGV es de :            $ ${igv} </h2>`);
document.write(`<hr> <h2> El valor total de la venta es de :  $ ${pv} </h2><hr>`);

console.table(`
El valor de la venta es de : $ ${vv}
El valor del IGV es de :  $ ${igv}
El valor total de la venta es de :  $ ${pv}
`)











