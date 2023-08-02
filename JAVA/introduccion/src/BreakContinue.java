public class BreakContinue {
        public static void main(String[] args) {

        for(int i = 0; i <= 20; i++) {
            System.out.print("\nValor de i : " + i);

            if (i == 5) {
                System.out.println("\nEn este punto se hace un salto a la siguiente iteraci\u00F3n");
                continue;

            } else {
                if (i == 10) {
                    System.out.println("\nEn este punto la función es detenida");
                    break;
                }
            }
        }
    }
}
