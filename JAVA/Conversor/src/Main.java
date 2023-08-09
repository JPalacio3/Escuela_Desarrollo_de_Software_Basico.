import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner leer = new Scanner(System.in);

        EXTERNA: // Etiqueta para romper el ciclo while y el ciclo switch al seleccionar 'Salir'
        while (true) {
            System.out.println("===== CONVERSOR DE MONEDAS =====");
            System.out.println(
                    "1 - Soles Peruanos a Dólares\n" +
                    "2 - Pesos Mexicanos a Dólares\n" +
                    "3 - Pesos Colombianos a Dólares\n" +
                    "4 - Salir" );

            System.out.print("SELECCIONE UNA OPCIÓN: ");
            char opcion = leer.next().charAt(0);

            switch (opcion) {
                case '1':
                    convertir(3.58, "Soles Peruanos");
                    break;
                case '2':
                    convertir(22.15, "Pesos Mexicanos");
                    break;
                case '3':
                    convertir(3851.90, "Pesos Colombianos");
                    break;
                case '4':
                    System.out.println(" CERRANDO PROGRAMA");
                    leer.close(); // Cerrar Scanner aquí
                    break EXTERNA;
                default:
                    System.out.println("OPCIÓN INCORRECTA");
                    break;
            }
        }
    }

    static void convertir(double valorDolar, String pais) {
        Scanner leer = new Scanner(System.in);
        System.out.printf("Ingrese la cantidad de %s : ", pais);
        double cantidadMoneda = leer.nextDouble();

        double dolares = cantidadMoneda / valorDolar;
        dolares = (double) Math.round(dolares * 100d) / 100;

        System.out.println("======================================");
        System.out.println("||     Tienes $ " + dolares + " Dólares     ||");
        System.out.println("======================================");
    }
}
