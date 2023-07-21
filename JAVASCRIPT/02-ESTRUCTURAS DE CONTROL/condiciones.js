if (false) {
    console.log('Se cumple la condición')
} else {
    console.log('No se cumple la condición');
}


// Ejercicio para comprobar si un número es par o impar
let n = -79;
let print = '';

// if (n % 2 == 0) {
//     print = `El número ${n} es par;`
// } else {
//     print = `El número ${n} es impar;`
// }

// Ejercicio para anidar varias comprobaciones dentro de una sola:

if (n !== 0) {
    if (n > 0) {
        if (n % 2 === 0) {
            print = `El número ${n} es PAR POSITIVO`;
        } else {
            print = `El número ${n} es IMPAR POSITIVO`;
        }
    } else {
        if (n % 2 === 0) {
            print = `El número ${n} es PAR NEGATIVO`;
        } else {
            print = `El número ${n} es IMPAR NEGATIVO`;
        }
    }
} else {
    print = `El número ${n} es NEUTRO`;
}

console.log(print);
