
// Clase Main
public class Main {
    public static void main(String []args) {
        String nombre;
        int a, b, c;

        nombre = "Joel";
        int edad = 33;
        a = 1;
        b = 2;
        c = 3;

        System.out.println(nombre);
        System.out.println(edad);

        // Modificar el valor de una variable
        edad = 30;
        System.out.println(edad);

        System.out.println(a + b + c);

        // Nueva forma de definir las variables
        var primerNombre = "Alberto ";
        System.out.println(primerNombre);

        var segundoNombre = "Joel ";
        var misNombres = segundoNombre + primerNombre;
        System.out.println("Mi nombre es " + misNombres);

        // DEFINIR OTRO TIPO DE VARIABLES
        // byte
        byte edad1 = 23;
        System.out.println(edad1);

        // long
        long numeroGrande = 12548474841L; // Añadimos una L al fimal para indicar que es un número grande
        System.out.println(numeroGrande);

        // float
        float nd = 3.5f; // Añadimos una f al final para indicar que es un número flotante
        System.out.println(nd);

        // double
        double ndd = 3.55d; // Opcional añadir la d al final para indicar que es un número decimal más grande
        System.out.println(ndd);

        // char
        char letra = 'a';
        char codigo = 65; // Para un solo caracter se puede insertar el código ASCII
        System.out.println(codigo);
        System.out.println(letra);

        // Boolean
        boolean opcion1 = true;
        boolean opcion2 = false;
        System.out.println(opcion1);
        System.out.println(opcion2);

        /*
        String es un objeto en java que se usa para almaenar adenas de
        caracteres, NO ES UN DATO PRIMITIVO
        */
        String nombreCompleto = "Joel Alberto Palacio Cano";
        System.out.println(nombreCompleto);

        // OPERADORES MATEMATICOS
        a = 10;
        b = 20;
        System.out.println(a + b);
        System.out.println(a - b);
        System.out.println(a * b);
        System.out.println(a / b);
        System.out.println(a % b);


        // OPERADORES EN ASIGNACIÓN
        a = 20;
        a = a += 5;
        System.out.println(a);
        a = a -= 5;
        System.out.println(a);
        a = a *= 5;
        System.out.println(a);
        a = a /= 5;
        System.out.println(a);
        a = a %= 5;
        System.out.println(a);

    }
}






