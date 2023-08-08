// Aplicación para detetar palabras palíndromas

import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner leer = new Scanner(System.in);
        System.out.println(" Ingrese una palabra: ");
        String cadena = leer.nextLine();

        if (esPalindromo(cadena)) {
            System.out.println("==============================");
            System.out.println(cadena + " Es PALÍNDROMA ");
            System.out.println("==============================");
        } else {
            System.out.println("==============================");
            System.out.println(cadena + " NO Es PALÍNDROMA ");
            System.out.println("==============================");

        }

        leer.close();
    }

    static boolean esPalindromo(String cadena) {

        cadena = cadena.replace(" ", "");
        cadena = cadena.toLowerCase();

        StringBuilder cadenaInvertida = new StringBuilder();

        for (int i = cadena.length() - 1; i >= 0; i--) {
            cadenaInvertida.append(cadena.charAt(i));
        }

        return cadena.equals(cadenaInvertida.toString());
    }
}
