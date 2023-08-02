
import java.util.Scanner;

public class Esvocal {

    public static void main(String[] args) {
        Scanner leer = new Scanner(System.in);

        System.out.print("Ingrese una letra: ");
        String c = leer.nextLine();

        if (c.equals("A") || c.equals("a")) {
            System.out.printf("%s ES VOCAL\n", c);
        } else if (c.equals("E") || c.equals("e")) {
            System.out.printf("%s ES VOCAL\n", c);
        } else if (c.equals("I") || c.equals("i")) {
            System.out.printf("%s ES VOCAL\n", c);
        } else if (c.equals("O") || c.equals("o")) {
            System.out.printf("%s ES VOCAL\n", c);
        } else if (c.equals("U") || c.equals("u")) {
            System.out.printf("%s ES VOCAL\n", c);
        } else {
            System.out.printf("%s NO ES UNA VOCAL\n", c);
        }
        leer.close();
    }
}

/*
En Java, la comparación de cadenas con el operador == compara las referencias de objetos y no los valores de las cadenas. Para comparar el contenido de las cadenas, debes utilizar el método equals().

if (c.equals("A") || c.equals("a")) {
    System.out.printf("%s ES VOCAL\n", c);
}
*/
