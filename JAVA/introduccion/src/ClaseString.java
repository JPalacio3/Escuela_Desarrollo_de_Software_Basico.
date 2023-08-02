public class ClaseString {
    public static void main(String[] args) {

        String nombre = "Joel";
        System.out.println(nombre.charAt(2)); // e
        System.out.println("cantidad de Caracteres: " + nombre.length()); // cantidad de Caracteres: 4

        for (int i = 0; i < nombre.length(); i++) {
            System.out.println(nombre.charAt(i)); // J o e l
        }

        System.out.println(nombre.substring(0, 3)); // Joe
        System.out.println(nombre.toLowerCase()); // joel
        System.out.println(nombre.toUpperCase()); // JOEL

        nombre = "A l b e r t o";
        System.out.println(nombre.replace(" ", "-")); // A-l-b-e-r-t-o
        System.out.println(nombre.replace(" ", "")); // Alberto

        System.out.println("Hola".equals("hola")); // false

        // Clase StringBuilder
        StringBuilder nuevo = new StringBuilder();
        System.out.println(nuevo.toString()); // Imprime un objeto vacío

        nuevo.append("Hola ");
        System.out.println(nuevo); // Hola
        nuevo.append("Mundo");
        System.out.println(nuevo.toString()); // Hola Mundo



    }
}
