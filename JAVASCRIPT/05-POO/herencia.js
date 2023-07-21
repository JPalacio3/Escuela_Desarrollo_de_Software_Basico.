// Superclase

// OBJETO 1
class Animal {
    constructor(nombre) {
        this.nombre = nombre;
    }

    saludar() {
        console.log(`Hola, soy ${this.nombre}.`);
    }
}

// Subclase
class Perro extends Animal {
    constructor(nombre,raza) {
        super(nombre); // Llamada al constructor de la superclase
        this.raza = raza;
    }

    ladrar() {
        console.log("¡Guau, guau!");
    }

    saludar() {
        console.log(`¡Hola! Soy ${this.nombre}, un perro de raza ${this.raza}.`);
    }
}

// Creación de objetos
const animal1 = new Animal("Animalito");
const perro1 = new Perro("Bobby","Labrador");

animal1.saludar(); // Hola, soy Animalito.
perro1.saludar(); // ¡Hola! Soy Bobby, un perro de raza Labrador.
perro1.ladrar(); // ¡Guau, guau!



// OBJETO 2
class Persona {
    constructor(nombre,edad) {
        this.nombre = nombre;
        this.edad = edad;
    }

    detallePersona() {
        console.log(`Nombre: ${this.nombre} \n Edad: ${this.edad} años.`);
    }
}

class Empleado extends Persona {
    constructor(nombre,edad,sueldo);
    super(nombre,edad) {
        this.sueldo = sueldo;

    }
    detallePersona() {
        super.detallePersona();
        console.log('sueldo:',this.sueldo);
    }
}

const emp1 = new Empleado('Joel',33,25000);
emp1.detallePersona();
console.log(emp1)




