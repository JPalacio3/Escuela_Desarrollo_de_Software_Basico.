// Funciones
function saludar() {
    console.log("Hola mundo desde la función saludar");
}
saludar();

// Funciones con parámetros y argumentos
function saludo(nombre) {
    console.log(`Hola, ${nombre} desde la función saludo`)
}
saludo('Joel');

// Funciones con retorno
function hola(name) {
    return `Hola, ${name} desde la función hola`;
}
const s = hola('JOEL');
const r = hola('ALBERTO');
console.log(s);
console.log(r);

// Valores predeterminados de parámtreos y funciones
function sumar(a = null,b = null) {
    if (a == null || b == null) {
        console.log('Es obligatorio declarar dos números para poder sumar')
        return;
    }
    return a + b;
}
let suma = sumar(40,50);
console.log(suma);
