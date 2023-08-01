
// Importar la clase scanner
import java.util.Scanner;

public class EntradaDatos {
    public static void main(String[] args) {
        Scanner leer = new Scanner(System.in);

            System.out.println("Ingrese su nombre: ");
            String nombre = leer.nextLine();

            System.out.println("Ingrese su edad");
            int edad = leer.nextInt();

            System.out.println("Ingrese un caracter: ");
            char c = leer.next().charAt(0);

            System.out.println("Su Nombre es: " + nombre + ". Y su edad es: " + edad + " años");
            System.out.println("Caracter: " + c);
        }
    }

    /*
    Ingrese su nombre:
        Joel
        Ingrese su edad
        33
        Ingrese un caracter:
        Joel
        Su Nombre es: Joel. Y su edad es: 33 años
        Caracter: J
    */
