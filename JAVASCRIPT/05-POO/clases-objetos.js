

class Persona {

    // Creación de un constructor, en donde definimos las propiedades que recibe dicho objeto
    constructor(nombre,edad) {
        this.nombre = nombre;
        this.edad = edad;
    }

    //Métodos o comportamientos de los objetos
    imprimir() {
        console.log(this.nombre,this.edad);

    }

}

const p1 = new Persona('Joel',33); //  Cunado estamos instanciando o creando un nuevo objeto de la clase, es cuando se ejecuta el constructor
const p2 = new Persona('Alberto',33);

console.log(p1);
console.log(p2);
p1.imprimir();
p2.imprimir();
