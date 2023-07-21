/*
PRÁCTICA 01 : DESCUENTOS DE UN RESTAURANTE

ENUNCIADO:
Un restaurante ofrece un descuento del 10% para consumo de hasta s/. 100.00 y un descuento del 20% para consumos mayores, para ambos casos se aplica un impuesto del 19%.
Determinar el monto del descuento, el impuesto y el importe a pagar

* monto del descuento
* impuesto
* importe a pagar
*/

// Entrada de datos
let consumo = Number(prompt('Ingrese el consumo'));
let descuento,datoDescuento;

// Proceso
if (consumo <= 100) {
    //Aplicar descuento del 10%
    datoDescuento = '10%';
    descuento = consumo * 0.10;
} else if (consumo > 100) {
    // Aplicar descuento del 20%
    datoDescuento = '20%';
    descuento = consumo * 0.20;
}

// Calcular descuento, impuesto y monto a pagar
let montoDescuento = consumo - descuento;
let igv = montoDescuento * 0.19;

let totalPagar = montoDescuento + igv;

// Salida de datos
document.write(`<pre>
Consumo             : ${consumo} s/.
Descuento           : ${datoDescuento} s/.
monto con descuento : ${montoDescuento} s/.
IGV                 : ${igv} s/.
Total a Pagar       : ${totalPagar} s/.

</pre>
`);
