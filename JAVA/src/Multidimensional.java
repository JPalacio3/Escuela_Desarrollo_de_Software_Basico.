public class Multidimensional {
    public static void main(String[] args) {

        int[][] x = new int[2][3];

        // PRIMER ARRAY CON DOS FILAS Y TRES COLUMNAS
        x[0][0] = 1;
        x[0][1] = 2;
        x[0][2] = 3;

        x[1][0] = 4;
        x[1][1] = 5;
        x[1][2] = 6;

        for (int[] matrizInterna : x) {
            for (int dato : matrizInterna) {
                System.out.println(dato);
            }
        }
        /*
        SALIDA:
        1
        2
        3
        4
        5
        6
        */

        // SEGUNDO ARRAY CON TRES FILAS Y TRES COLUMNAS:
        int[][] y = {
            {1,2,3},
            {4,5,6},
            {7,8,9},
        };

        for (int[] matriz : y) {
            for (int dato : matriz) {
                System.out.println(dato);
            }
        }
        /*
        SALIDA:
        1
        2
        3
        4
        5
        6
        7
        8
        9
        */


        // ARRAY TRIDIMENSIONAL
        int [][][] z = {
            {
                { 1, 2, 3 },
                { 4, 5, 6 },
            },
            {
                { -1, -5, -3 },
                { -4, -5, -6 }
            }
        };
        for (int[][] matriz2D : z) {
            for (int[] matriz1D : matriz2D) {
                for (int dato : matriz1D)
                    System.out.println(dato);
            }
        }

        /*
        SALIDA:
        1
        2
        3
        4
        5
        6
        -1
        -5
        -3
        -4
        -5
        -6
        */

    }
}

/*
Para iterar sobre los elementos de un array bidimensional en Java, puedes utilizar bucles anidados. Un bucle anidado te permitirá recorrer cada fila y columna de la matriz y acceder a sus elementos. En tu caso, dado que tienes un array bidimensional x de tamaño 2x3, necesitas dos bucles anidados para recorrer todas las filas y columnas.
 */
