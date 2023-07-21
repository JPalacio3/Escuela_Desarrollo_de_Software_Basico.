/*
PRACTICA 03

Crea 3 arreglos y un arreglo que tendrá números del 1 al 9.
El primer array se llamará pares y segundo impar, ambos estarán vacíos
Después multiplica cada uno de los números del array con números por un número aleatorio entre 1 y 100, si el resultado es par se guarda ese número en el array de pares y si es impar en el array de impares. Muestra por consola: -la multiplicación que se produce junto con su resultado en el fofrmato 2 x 3 = 6 y el array de pares e impares.

*/

// Craeción de los arreglos
let pares = [];
let impar = [];
let numeros = [ 1,2,3,4,5,6,7,8,9 ];
let numeroRandom = 0;


// Calculo de las multiplicaciones
for (let n of numeros) {
    numeroRandom = parseInt((Math.random() * 100));
    let r = n * numeroRandom;

    if (r % 2 == 0) {
        console.log(`${n} x ${numeroRandom} = ${r} `);
        pares.push(r);
    } else if (r % 2 == 1) {
        console.log(`${n} x ${numeroRandom} = ${r} `);
        impar.push(r);
    }
}

// Mostrar por consola los arrays despues de los cálculos
console.log('ARRAY DE PARES : ',pares);
console.log('ARRAY DE IMPARES : ',impar);
