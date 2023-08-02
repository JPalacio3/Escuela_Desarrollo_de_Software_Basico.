import java.util.Scanner;

public class SalidaDatos {
    public static void main(String [] args)  {

        Scanner leer = new Scanner(System.in);

        System.out.print("Ingrese su nombre: ");
        String nombre = leer.nextLine();

        System.out.print("Ingrese su edad: ");
        int edad = leer.nextInt();

        System.out.print("Ingrese un caracter: ");
        char c = leer.next().charAt(0);

        System.out.printf("NOMBRE: %s EDAD: %d", nombre, edad );
        System.out.print(" Caracter: " + c);

        leer.close();
    }
}
/*
Ingrese su nombre: Joel
Ingrese su edad: 33
Ingrese un caracter: Joel
NOMBRE: Joel EDAD: 33 Caracter: J
*/
