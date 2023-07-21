
// Esto es una clases y se tiene que instanciar, no usar como una función (Esta es la forma anterior de usar clases en Js)
function Persona(nombre,edad) {
    this.nombre = nombre;
    this.edad = edad;

    this.imprimir = function () {
        console.log(`${this.nombre} ${this.edad}`);
    }
}

const p1 = new Persona('Joel',33);
const p2 = new Persona('Alberto',33);

console.log(p1.nombre)
console.log(p2.edad)
p1.imprimir();
p2.imprimir();
