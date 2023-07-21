// let : Sus valores pueden ser modificables

let nombre = 'Joel'; // las variables se usan como contenedores al que se les atribuye un valor, se separa un espacio en memoria y se les asigna dicho valor

// Imprimir en el documento el valor de la variable
document.write(nombre);

// Combinar html y mostrar el valor de la variable por medio de query strings
document.write(`<h1>${nombre}</h1>`);

let apellido = 'ALBERTO';

document.write(nombre + ' ' + apellido);
document.write(`<h1>${nombre + ' ' + apellido}</h1>`);



// Constantes: Sus valores no son modificables
const pais = 'México';

document.write(pais);
document.write(`<h1>${pais}</h1>`);
