class Persona {
    #nombre;
    #edad;
    constructor(nombre,edad) {
        this.#nombre = nombre;
        this.#edad = edad;
        this.#metdoPrivado();
    }

    set setNombre(nombre) {
        this.#nombre = nombre;
    }
    get getNombre() {
        return this.#nombre;
    }
    set setEdad(edad) {
        this.#edad = edad;
    }
    get getEdad() {
        return this.#edad;
    }

    #metdoPrivado() {
        console.log('Soy un método Privado');
    }
}

const p1 = new Persona('Joel',33);
console.log(p1);
p1.setNombre = 'Alberto';
console.log(p1);

