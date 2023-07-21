const palindromo = (palabra) => {

    palabra = palabra.replace(' ','');
    palabra = palabra.toLowerCase();

    let palabraInvertida = palabra.split('').reverse().join('');

    // console.log(palabrainvertida);

    if (palabra == palabraInvertida) {
        return true;
    } else {
        return false;
    }
}

// console.log(palindromo('Luz azul'));

let palabra = prompt('Ingrese una palabra');

let esPalindromo = palindromo(palabra);

if (esPalindromo) {
    document.write(`
    <h1>
    ${palabra} es un palíndromo
    </h1>`);
} else {
    document.write(`<h1>
    ${palabra} NO es un palíndromo
    </h1>`);
}

