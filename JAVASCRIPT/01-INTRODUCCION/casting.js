// El casting de daros hace referencia a la conversión de un dato a otro tipo de dato
// EJ :
// a String => String(),toString()
// a Números => Number(),parseInt()
// a Decimal => Number(),parseFloat()

// De entero a String
let dato = 33;

// 1. Vemos el tipo de dato que es
console.log(typeof (dato)); // Number

// 2. Convertimos el tipo de dato
dato = String(dato);
console.log(typeof (dato)); // String

// De String a Número
let dato2 = '45';
console.log(typeof (dato2)); // String

dato2 = parseInt(dato2);
console.log(typeof (dato2)); // Number
