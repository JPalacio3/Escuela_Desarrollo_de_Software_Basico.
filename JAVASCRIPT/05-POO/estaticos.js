class Mate {
    static #pi = Math.PI;

    static get PI() {
        return this.#pi;
    }

    static suma(a,b) {
        return a + b;
    }
}

console.log(Mate.PI);
console.log(Mate.suma(Mate.PI,2))
