public class Arrays {

    public static void main(String[] args) {
        String[] nombres = new String[3];

        nombres[0] = "Joel";
        nombres[1] = "Alberto";
        nombres[2] = "Palacio";

        System.out.println(nombres[1]); // Alberto

        nombres[2] = "Cano";
        System.out.println(nombres[2]); // Cano

        System.out.println(nombres.length); // 3
        System.out.println(nombres[1]); // Alberto

        int[] array1 = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };
        System.out.println(array1[5]); // 6
        System.out.println(array1.length); // 10

    }
}
