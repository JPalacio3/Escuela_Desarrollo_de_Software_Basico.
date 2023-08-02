public class Relacionales {

    public static void main(String [] args)
    {
        int a = 3;
        int b = 2;

        // OPERADORES RELACIONALES
        System.out.println(a == b); // false
        System.out.println(a != b); // true
        System.out.println(a < b); // false
        System.out.println(a > b); // true
        System.out.println(a <= b); // false
        System.out.println(a >= b); // true

        // OPERADORES LÓGICOS
        System.out.println(!true); // false
        System.out.println(!false); // true
        System.out.println(true && true); // true
        System.out.println(false); // false
        System.out.println(true && false); // false

        System.out.println(true); // true
        System.out.println(false || false); // false
        System.out.println(true); // true

        System.out.println(a == b  &&  a > b); // false
        System.out.println( !(a == b)  &&  a > b); // true
        System.out.println( a == b || a > b); // true
    }
}
