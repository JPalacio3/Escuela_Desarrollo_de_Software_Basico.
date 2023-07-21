function sumar(...args) {
    let suma = 0;

    for (let n of args) {
        suma += n;
    }
    return suma;
}

const s = sumar(50,50);
console.log('La suma es : ',s);
