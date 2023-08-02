public class ForEach {
    public static void main(String[] args) {

        String[] nombres = { "Joel", "Alberto", "Palacio", "Cano" };

        // WHILE :
        int c = 0;
        while (c < nombres.length) {
            System.out.println(nombres[c]);
            c++;
        }

        // FOR :
        for (int i = 0; i < nombres.length; i++) {
            System.out.println(nombres[i]);
        }

        // FOR EACH :
        for (String dato : nombres) {
            System.out.println(dato);
        }
    }
}
