// APLICACIÓN PARA DETECTAR PRIMALIDAD DE NÚMEROS

import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner leer = new Scanner(System.in);
        System.out.println("Ingrese un número entero : ");
        int numero = leer.nextInt();

        if (esPrimo(numero)) {
            System.out.println("====================");
            System.out.println(numero + " Es un número Primo");
            System.out.println("====================");

        } else {
            System.out.println("====================");
            System.out.println(numero + " No es un Número Primo");
            System.out.println("====================");
        }

        leer.close();
    }

    static boolean esPrimo(int numero) {

        int contador = 0;

        int[] numeros = new int[numero];

        for (int i = 0; i < numeros.length; i++) {
            numeros[i] = i + 1;
        }

        for (int i : numeros) {
            if (i == 1 || i == numero) {
                continue;
            }

            if (numero % i == 0) {
                contador++;
            }

        }

        return contador == 0;
}
}
