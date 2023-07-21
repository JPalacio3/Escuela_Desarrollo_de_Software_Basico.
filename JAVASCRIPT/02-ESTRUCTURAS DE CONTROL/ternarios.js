// Los operadores ternarios en JavaScript son una forma compacta de realizar una evaluación condicional en una sola línea.También se les conoce como operadores condicionales.

// La sintaxis básica de un operador ternario es la siguiente:
// condicion ? expresion_si_verdadera : expresion_si_falsa;


let n = -8;

let r = (n > 0) ? 'Es positivo' : ' Es Negativo';

console.log(r);


let v = 'z';

let salida = (v === 'a' || v === 'A') ? `${v} Es una Vocal`
    : (v === 'e' || v === 'E') ? `${v} Es una Vocal`
        : (v === 'i' || v === 'I') ? `${v} Es una Vocal`
            : (v === 'o' || v === 'O') ? `${v} Es una Vocal`
                : (v === 'u' || v === 'U') ? `${v} Es una Vocal`
                    : `${v} NO ES UNA VOCAL`;

console.log(salida);
