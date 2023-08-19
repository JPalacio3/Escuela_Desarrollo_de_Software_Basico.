import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

        OUTER:
        while (true) {
            // Presentación del juego y opciones de nivel
            System.out.println("\n   JUEGO ADIVINA EL NÚMERO   \n");
            System.out.println(
                "1 - Nivel Fácil      ( 10 Vidas ) \n"
                + "2 - Nivel Intermedio ( 7 Vidas ) \n"
                + "3 - Nivel Difícil    ( 5 Vidas )  \n"
                + "4 - SALIR"
            );

            // Capturar la opción seleccionada por el usuario
            Scanner leer = new Scanner(System.in);
            System.out.print("INGRESE UNA OPCIÓN : ");
            int opcion = leer.nextInt();

            // Evaluar la opción seleccionada
            switch (opcion) {
                case 1:
                    jugar(10); // Iniciar el juego en el nivel fácil con 10 vidas
                    break;
                case 2:
                    jugar(7);  // Iniciar el juego en el nivel intermedio con 7 vidas
                    break;
                case 3:
                    jugar(5);  // Iniciar el juego en el nivel difícil con 5 vidas
                    break;
                case 4:
                    System.out.println("CERRANDO EL PROGRAMA ... ");
                    break OUTER; // Salir del juego y cerrar el programa
                default:
                    System.out.println("Opción incorrecta");
            }
        }
    }

    static void jugar(int vidas) {
        int numeroRandom = (int) (Math.random() * 101);
        int numeroElegido = -1;

        // Mostrar la cantidad de vidas disponibles al inicio del juego
        System.out.printf("\n HAS CONSEGUIDO %d VIDAS \n", vidas);

        Scanner leer = new Scanner(System.in);

        while (numeroElegido != numeroRandom) {
            System.out.print("\nIngrese un número entre 1 y 100 : ");
            numeroElegido = leer.nextInt();

            // Comparar el número elegido con el número aleatorio y ajustar las vidas
            if (numeroRandom < numeroElegido) {
                System.out.println("\nEl número es más pequeño ! \n ");
                vidas--;
            } else if (numeroRandom > numeroElegido) {
                System.out.println("\nEl número es más Grande ! \n ");
                vidas--;
            }

            // Verificar si se han agotado las vidas
            if (vidas == 0) {
                System.out.println("\n-------------------------------");
                System.out.println("||||  PERDISTE EL JUEGO ||||");
                System.out.println("-------------------------------\n");
                break;
            }
            System.out.printf("\n TE QUEDAN %d VIDAS \n", vidas);
        }

        // Mostrar mensaje de victoria si se adivina el número
        if (numeroElegido == numeroRandom) {
            System.out.println("\n -------------------------------");
            System.out.println("||||||  FELICIDADES, GANASTE EL JUEGO  |||||| ");
            System.out.println("-------------------------------\n");
        }
    }
}
