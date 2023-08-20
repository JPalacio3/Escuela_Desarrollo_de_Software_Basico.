package clases;

// Definición de la clase Calculadora
public class Calculadora {
    // Declaración de una variable estática y constante llamada PI
    public static final double PI = 3.141592; // Esta constante representa el valor de PI
    // La instrucción final indica que el valor de esa variabkle es constante y no
    // se puede modificar

    // Definir un método para ejecutar una suma
    public static int sumar(int a, int b) {
        return a + b;
    }

    public static double sumar(double a, double b) {
        return a + b;
    }

    // Sobrecarga de métodos
    public int resta(int a, int b) {
        return a - b;
    }

    public double resta(double a, double b) {
        return a - b;
    }
}
