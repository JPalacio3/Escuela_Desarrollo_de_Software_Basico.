import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

        OUTER:
        while (true) {
            System.out.println("\n   JUEGO ADIVINA EL NÚMERO   \n");
            System.out.println(
                "1 - Nivel Fácil      ( 10 Vidas ) \n"
                + "2 - Nivel Intermedio ( 7 Vidas ) \n"
                + "3 - Nivel Difícil    ( 5 Vidas )  \n"
                + "4 - SALIR"
            );

            Scanner leer = new Scanner(System.in);
            System.out.print("INGRESE UNA OPCIÓN : ");
            int opcion = leer.nextInt();

            switch (opcion) {
                case 1:
                    jugar(10);
                    break;
                case 2:
                    jugar(7);
                    break;
                case 3:
                    jugar(5);
                    break;
                case 4:
                    System.out.println("CERRANDO EL PROGRAMA ... ");
                    break OUTER;
                default:
                    System.out.println("Opción incorrecta");
            }
        }
    }

    static void jugar(int vidas) {
        int numeroRandom = (int) (Math.random() * 101);
        int numeroElegido = -1;
        System.out.printf("\n HAS CONSEGUIDO %d VIDAS \n", vidas);

        Scanner leer = new Scanner(System.in);

        while (numeroElegido != numeroRandom) {
            System.out.print("\nIngrese un número entre 1 y 100 : ");
            numeroElegido = leer.nextInt();

            if (numeroRandom < numeroElegido) {
                System.out.println("\nEl número es más pequeño ! \n ");
                vidas--;
            } else if (numeroRandom > numeroElegido) {
                System.out.println("\nEl número es más Grande ! \n ");
                vidas--;
            }

            if (vidas == 0) {
                System.out.println("\n-------------------------------");
                System.out.println("||||  PERDISTE EL JUEGO ||||");
                System.out.println("-------------------------------\n");
                break;
            }
            System.out.printf("\n TE QUEDAN %d VIDAS \n", vidas);
        }

        if (numeroElegido == numeroRandom) {
            System.out.println("\n -------------------------------");
            System.out.println("||||||  FELICIDADES, GANASTE EL JUEGO  |||||| ");
            System.out.println("-------------------------------\n");
        }
    }
}
