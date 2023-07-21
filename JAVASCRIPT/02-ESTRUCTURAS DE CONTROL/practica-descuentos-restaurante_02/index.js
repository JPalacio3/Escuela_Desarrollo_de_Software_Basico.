/*
PRÁCTICA 02: DESCUENTOS DE UN RESTAURANTE PARTE 02

ENUNCIADO:
Debido a los excelentes resultaods, el restaurante decide ampliar sus ofertas de acuerdo a la siguiente escala de consumo.
Determinar el monto del descuento, el importe del impuesto y el importe a pagar:

Consumo (S/.)      Descuento
*Hasta 100    ----->  10
*Mayor a 100  ----->  20
*Mayor a 200  ----->  30

ANÁLISIS:
Para la solución de este problema, se requiere que el usuario ingrese el consumo y el sistema verifica y calcula el monto del descuento, el impuesto y el importe a pagar
*/


// Entrada de datos
let consumo = Number(prompt('Ingrese el consumo'));
let descuento,datoDescuento;

// Proceso
if (consumo <= 100) {
    //Aplicar descuento del 10%
    datoDescuento = '10%';
    descuento = consumo * 0.10;
} else if (consumo > 100 && consumo <= 200) {
    // Aplicar descuento del 20%
    datoDescuento = '20%';
    descuento = consumo * 0.20;
} else if (consumo > 200) {
    // Aplicar descuento del 30%
    datoDescuento = '30%';
    descuento = consumo * 0.30;
}

// Calcular descuento, impuesto y monto a pagar
let montoDescuento = consumo - descuento;
let igv = montoDescuento * 0.19;

let totalPagar = montoDescuento + igv;

// Salida de datos
document.write(`<pre>
Consumo             : ${consumo} s/.
Descuento           : ${descuento} s/.  ( ${datoDescuento} )
monto con descuento : ${montoDescuento} s/.
IGV                 : ${igv} s/.  (19%)
Total a Pagar       : ${totalPagar} s/.

</pre>
`);
