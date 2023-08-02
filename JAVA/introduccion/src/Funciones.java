public class Funciones {
    public static void main(String[] args) {

        // Invocación de la función externa
        saludar();

        // Invocación de las funciones con parámetros y argumentos
        sumar(5, 4);

        saludo("Joel", 33);

        // Invocación de las funciones con retorno
        System.out.println(hola("Joel", 33));

        System.out.println(suma(4, 5));
        // Invocaciónd e la función con sobrecarga
        System.out.println(suma(4.5, 1.3));

        // Invocación de las funciones recursivas
        CuentaRegresiva(20);

        System.out.println(factorial(5));

        // Invocación de la función con varargs
        System.out.println(sumar(5,5,5,5,5,5,5,5,5,5,5,5,5,5));



    }

    // Definición de una función externa : void indica que se va a ejecutar sin retornar nada
    static void saludar() {
        System.out.println("Hola mundo");
    }

    // Función con parámetros y argumentos
    static void sumar(int a, int b) {
        int suma = a + b;
        System.out.printf("La suma:  %d + %d = %d\n", a, b, suma);
    }

    static void saludo(String nombre, int edad) {
        System.out.printf("Hola %s, tu edad es %d años, Bienvenido!\n", nombre, edad);
    }
    // Función con retorno: Se pone en la definicón dela función el tipo de dato que va a retonar (String en este caso)
    static String hola(String nombre, int edad) {
        return "Hola, su nombre es " + nombre + " y su edad es " + edad + " años";
    }

    // Función con retorno: Se pone en la definicón dela función el tipo de dato que va a retonar (int en este caso)
    static int suma(int a, int b) {
        return a + b;
    }

    // Sobrecarga de funciones ( overloading ) : auqnue tenga el mismo nombre que otra función, debe tener algún parámetro diferente en su definición
    static double suma(double a, double b) {
        return a + b;
    }

    // Función Recursiva: se ejecuta a sí misma hasta cumplr una condición
    static void CuentaRegresiva(int numero) {
        numero--;

        if (numero > 0) {
            System.out.println(numero);
            CuentaRegresiva(numero);
        } else {
            System.out.println("La cuenta ha llegado hasta 0");
        }
    }

    static int factorial(int numero) {
        if (numero > 1) {
            numero = numero * factorial(numero - 1);
        }
        return numero;
    }

    // VARAGS : Son las funiones a las que se les puede asignar pa´rametros indefinidos
    static int sumar(int... numeros) {
        int suma = 0;
        for (int num : numeros) {
            suma += num;
        }
        return suma;
    }

}
