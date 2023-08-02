public class ClaseMath {
    public static void main(String[] args) {

        System.out.println(Math.PI); // 3.141592653589793
        System.out.println(Math.E); // 2.718281828459045

        System.out.println(Math.pow(5, 3)); // 125.0

        System.out.println(Math.random()); // devuelve un número random entre 0 y 1

        int numeroRandom = (int)(Math.random() * 100);
        System.out.println(numeroRandom); // Devuelve un número entero random entre 0 y 100

        System.out.println(Math.sqrt(25)); // 5.0
        System.out.println((int) (Math.sqrt(25))); // 5

        System.out.println(Math.max(8, 9)); // 9
        System.out.println(Math.min(8, 9)); // 8

        System.out.println(Math.round(5.8456)); // 6

        double moneda = (double) Math.round(3.47524115 * 100d) / 100;
        System.out.println(moneda); // 3.48

    }
}
