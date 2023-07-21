
/*
En JavaScript,existen varios tipos de operadores que se utilizan para realizar diferentes tipos de operaciones.Los operadores se pueden clasificar en diferentes categorías:

1. ** Operadores aritméticos **: se utilizan para realizar operaciones matemáticas en valores numéricos.Los operadores aritméticos incluyen ** `+` ** (suma), ** `` ** (resta), ** `` ** (multiplicación), ** `/` ** (división), ** `%` ** (módulo) y ** `*` ** (exponente).
2. ** Operadores de asignación **: se utilizan para asignar valores a variables.El operador de asignación básico es ** `=` **.También existen operadores de asignación compuestos,como ** `+=` **, ** `=` **, ** `=` **, ** `/=` ** y ** `%=` **.
3. ** Operadores de comparación **: se utilizan para comparar dos valores y devolver un resultado booleano(** `true` ** o ** `false` **).Los operadores de comparación incluyen ** `==` ** (igualdad), ** `!=` ** (desigualdad), ** `===` ** (igualdad estricta), ** `!==` ** (desigualdad estricta), ** `>` ** (mayor que), ** `<` ** (menor que), ** `>=` ** (mayor o igual que) y ** `<=` ** (menor o igual que).
4. ** Operadores lógicos **: se utilizan para combinar expresiones booleanas y devolver un resultado booleano.Los operadores lógicos incluyen ** `&&` ** (AND lógico), ** `||` ** (OR lógico) y ** `!` ** (NOT lógico).
5. ** Operadores de concatenación **: se utilizan para concatenar cadenas de texto.El operador de concatenación es ** `+` **.
6. ** Operadores ternarios **: se utilizan para asignar un valor a una variable en función de una expresión booleana.El operador ternario tiene la siguiente sintaxis: ** `condición ? valor_si_verdadero : valor_si_falso` **.

Estos son algunos de los operadores más comunes en JavaScript,pero existen otros operadores más avanzados como el operador de objeto ** `.` ** y el operador de propagación ** `...` **.

Además de los operadores que mencioné anteriormente,hay otros operadores en JavaScript que son menos comunes,pero que pueden ser muy útiles en situaciones específicas.A continuación,te describo algunos de ellos:

1. ** Operador de objeto ** (** `.` **): se utiliza para acceder a las propiedades de un objeto.Por ejemplo:

let persona = { nombre: "Juan",edad: 30 };
let nombre = persona.nombre;
let edad = persona.edad;


1. ** Operador de propagación ** (** `...` **): se utiliza para descomponer objetos o arreglos en elementos individuales.Por ejemplo:
*/

let arreglo1 = [ 1,2,3 ];
let arreglo2 = [ 4,5,6 ];


// 1. ** Operador de tipo ** (** `typeof` **): se utiliza para obtener el tipo de dato de una variable.Por ejemplo:


let numero = 42;
let tipoDeDato = typeof numero;


// 1. ** Operador de instancia ** (** `instanceof` **): se utiliza para determinar si un objeto es una instancia de una clase en particular.Por ejemplo:


class Persona {
    constructor(nombre) {
        this.nombre = nombre;
    }
}

let persona1 = new Persona("Juan");
let esInstancia = persona1 instanceof Persona;


// 1. ** Operador de coma ** (** `,` **): se utiliza para separar varias expresiones en una sola línea de código.El resultado de la expresión es el valor de la última expresión en la lista.Por ejemplo:


let x = 1,y = 2,z = 3;
let resultado = (x += y,y += z,x + y + z);


// Estos son solo algunos de los operadores menos comunes en JavaScript,pero hay muchos más que se pueden utilizar en diferentes situaciones.
