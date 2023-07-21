let n = 2,i = 0;

// while (i <= 10) {
//     console.log(`${n} x ${i} = ${n * i}`);
//     i++;
// }


let texts = 'JavaScript';
// while (i < texts.length) {
//     console.log(texts[ i ]);
//     i++;
// }


let estudiantes = [ 'Alex','Roel','Joel','Alberto' ];
while (i < estudiantes.length) {
    console.log(` HOLA ${estudiantes[ i ]}, TE SALUDO DESDE UN CICLO WHILE DE JAVASCRIPT`);
    i++;
}


// DO-WHILE: El bucle do-while es una estructura de control similar al bucle while, pero con una diferencia fundamental: la condición se evalúa después de cada iteración. Esto significa que el bloque de código se ejecuta al menos una vez, sin importar si la condición inicial es verdadera o falsa.

let s = 0;
do {
    console.log('HOLA');
    s++;

} while (s <= 5);
