const persona = {
    nombre: 'Joel',
    apellido: 'Palacio',
    edad: '33',
    pais: 'Colombia',
    residencia: 'Mexico',

    nombreCompleto() {
        return `${this.nombre} ${this.apellido}`;
    },

    saludar() {
        return `Hola, mi nombre es ${this.nombreCompleto()}`
    },

    saludoCompleto() {
        return `Hola, mi Nombre es ${this.nombreCompleto()} tengo ${this.edad} años, soy un ciudadano del país ${this.pais}, pero resido hace 4 años en ${this.residencia} ...Saludos.`
    },

    trajes: [ 'traje1','traje2','traje3',],

    direccion: {
        calle: 'Santo Domingo',
        numero: '2069',
        colonia: 'Del Sur',
        ciudad: 'Guadalajara'
    },
}

console.log(persona.nombre)
console.log(persona.nombreCompleto());
console.log(persona.saludar());
console.log(persona.saludoCompleto());
console.log(persona.direccion);
console.log(persona.direccion.ciudad);
console.log(persona.trajes);
