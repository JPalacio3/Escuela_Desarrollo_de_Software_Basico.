let n = 5;

for (let i = 0;i <= 10;i++) {
    console.log(`${n} x ${i} = ${n * i}`);
}


let texts = 'Javascript';
let estudiantes = [ 'Alex','Roel','Joel','Alberto' ];

//Iterar sobre los elementos del arreglo y devuelve sus indices:
for (let dato in estudiantes) {
    console.log(dato);
}

//Iterar sobre los elementos del arreglo y recupera sus valores:
for (let dato of estudiantes) {
    console.log(`Hola ${dato}, te saludo desde un ciclo for en Javascript que te ha escogido al azar 😜`);
}
