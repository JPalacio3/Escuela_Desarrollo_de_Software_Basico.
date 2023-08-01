public class Incremento_decremento {


    public static void main(String[] args)
    {
        int c = 1;

        // INCREMENTO
        c++;
        c++;
        c++;
        c++;
        c++;
        System.out.println(c); // 6

        // DECREMENTO
        c--;
        c--;
        c--;
        c--;
        System.out.println(c); // 2

        // PREINCREMENTO : El incremento se ejecuta antes de la ejecución
        System.out.println(++c); // 3
        System.out.println(++c); // 4
        System.out.println(c); // 4

        // POSINCREMENTO : El incremento se lleva a cabo después de la ejecución
        System.out.println(c++); // 4
        System.out.println(c); // 5

        // PREDECREMENTO
        System.out.println(--c); // 4
        System.out.println(--c); // 3
        System.out.println(c); // 3

        // POSTDECREMENTO
        System.out.println(c--); // 3
        System.out.println(c--); // 2
        System.out.println(c); // 1

    }
}
