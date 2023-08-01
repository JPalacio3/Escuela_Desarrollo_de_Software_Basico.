package suma;
import java.util.Scanner;

public class Suma {
    public static void main(String[] args) {

        Scanner leer = new Scanner(System.in);

            System.out.print("Ingrese un número entero: ");
            int a = leer.nextInt();

            System.out.print("Ingrese otro número entero: ");
            int b = leer.nextInt();

            var r = a+b;
            System.out.printf("La suma de %d + %d es : %d\n ", a, b, r);

    }
}

