import java.util.Scanner;

public class BucleWhile {
    public static void main(String[] args) {
        int c = 10;

        // while (c <= 10) {
        //     System.out.println("El valor de C es " + c);
        //     c++;
        // }

        // Tabla de multiplicar:
        Scanner leer = new Scanner(System.in);
        System.out.println("Ingrese un número para mostrar su tabla de multiplicar: ");
        int n = leer.nextInt();
        while (c <= 50) {
            System.out.printf("| %d x %d = %d | \n", n, c, (n * c));
            c++;
        }
        leer.close();
    }
}
