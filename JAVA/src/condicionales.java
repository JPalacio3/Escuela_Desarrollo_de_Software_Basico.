
import java.util.Scanner;


// public class condicionales {
//     public static void main(String[] args) {
//         // ESTRUCTURA SECUENCIAL SIMPLE
//         if (true) {
//             System.out.println("Se cumple la condición");
//         } // Se cumple la condición

//         // ESTRUCTURA SECUENCIAL DOBLE
//         if (true) {
//             System.out.println("Se cumple la condicion");
//         } else {
//             System.out.println("NO se cumple la condición");
//         } // Se cumple la condición
//     }
// }


    // SISTEMA PARA DETECTAR SI UN NÚMERO ES PAR O IMPAR

public class condicionales {
    public static void main(String[] args) {

        Scanner leer = new Scanner(System.in);

        System.out.print("Ingrese un número entero: ");

        int n = leer.nextInt();

        if(n != 0) {
            if(n > 0){
                if (n % 2 == 0) {
                    System.out.printf("El número %d es PAR POSITIVO\n", n);
                }else {
                    System.out.printf("El número %d es IMPAR POSITIVO\n", n);
                }
            }else{
                if (n % 2 == 0) {
                    System.out.printf("El número %d es PAR NEGATIVO\n", n);
                }else{
                    System.out.printf("El número %d es IMPAR NEGATIVO\n", n);
                }
            }
        }else{
            System.out.printf("El número %d es NEUTRO\n", n);
        }
        leer.close();
    }
}
