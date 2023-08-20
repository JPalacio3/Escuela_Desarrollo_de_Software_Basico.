package clases;

public class Rectangulos {

    // Definir los atributos de la clase
    public int base;
    public int altura;

    // Crear el constructor
    public Rectangulos() {
        System.out.println(base);
        System.out.println(altura);
    }

    // Crear métodos
    public int area(int base, int altura) {
        this.base = base;
        this.altura = altura;
        return this.base * this.altura;
    }

    public int perimetro(int base, int altura) {
        this.base = base;
        this.altura = altura;
        return 2 * (this.base + this.altura);
    }
}
