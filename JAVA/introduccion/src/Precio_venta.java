
// CALCULAR EL PRECIO DE VENTA RECIBIENDO LA ENTRADA DEL VALOR DE LA VENTA Y CON UN IGV DE 18%

import java.util.Scanner;

public class Precio_venta {
    public static void main(String[] args) {
        // Crear un objeto Scanner para leer la entrada del usuario
        Scanner leer = new Scanner(System.in);

        // Solicitar al usuario que ingrese el valor de la venta
        System.out.println("Ingrese el PRECIO DE VENTA: ");
        double vv = leer.nextDouble();

        // Calcular el IGV (18% del valor de la venta)
        double igv = vv * 0.18;

        // Calcular el precio de venta sumando el valor de la venta y el IGV
        double pv = vv + igv;

        // Mostrar los resultados en la consola
        System.out.println("Valor de Venta : " + vv);
        System.out.println("IGV : " + igv);
        System.out.println("Precio de Venta : " + pv);

        leer.close();
    }
}
