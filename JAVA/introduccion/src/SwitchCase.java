import java.util.Scanner;

public class SwitchCase {


    public static void main(String[] args) {

        Scanner leer = new Scanner(System.in);

        System.out.print("Ingrese un número de la Semana (1 al 7): ");
        int dia = leer.nextInt();

        String nombreDia = null;

        switch (dia) {
            case 1:
                nombreDia = "Domingo";
                break;
            case 2:
                nombreDia = "Lunes";
                break;
            case 3:
                nombreDia = "Martes";
                break;
            case 4:
                nombreDia = "Miércoles";
                break;
            case 5:
                nombreDia = "Jueves";
                break;
            case 6:
                nombreDia = "Viernes";
                break;
            case 7:
                nombreDia = "Sábado";
                break;
            default:
                nombreDia = " [Número Inválido], escriba un número del 1 al 7 ";
        }
        System.out.println("El día de la semana seleccionado es " + nombreDia);

        leer.close();
    }
}
