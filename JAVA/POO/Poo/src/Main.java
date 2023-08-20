/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */

import clases.Calculadora;
import clases.Persona;
import clases.Rectangulos;
import static java.lang.Math.*;

/**
 *
 * @author JPalacio
 */
public class Main {

    public static void main(String[] args) {

        // Constructor de la clase Persona
        Persona persona3 = new Persona();
        Persona persona4 = new Persona("Joel");
        Persona persona5 = new Persona();
        persona5.nombre = "Joel Alberto";
        persona5.edad = 33;
        persona5.mostrarDatos();

        Persona persona1; // Creamos un objeto nuevo instanciando de la clase
        persona1 = new Persona(); // Asignamos el objeto a la clase padre, indicando que es una nueva instancia
        persona1.nombre = "Joel"; // Asignamos los valores de los atributos que contiene la clase
        persona1.edad = 33;
        persona1.mostrarDatos(); // Invocamos el método que contiene la clase para ejecutarla

        Persona persona2 = new Persona(); // Instanciamos el objeto de manera directa a la clase
        persona2.nombre = "Alberto";
        persona2.edad = 33;
        persona2.mostrarDatos();

        System.out.println(Calculadora.PI); // Ejecutamos el atributo PI de la clase calculadora(paquete clases)

        System.out.println(Calculadora.PI);

        System.out.println(Calculadora.sumar(40, 50)); // método sumar de la clase calculadora de enteros
        System.out.println(Calculadora.sumar(40.4, 50)); // método sumar de la clase calculadora de doubles

        // Para utilizar los métodos que no son estáticos, con sobrecarga de métodos,
        // debemos crear un objeto
        Calculadora calcular = new Calculadora();
        System.out.println(calcular.resta(20, 19));
        System.out.println(calcular.resta(20.2, 19.1));

        System.out.println(PI); // Importar la clase Math de java completa para usar sus atributos y métodos
        System.out.println(pow(4, 2));

        final int a = 10; // Es una variable constante, su valor no se puede modificar (final)
        System.out.println(a);

        Rectangulos r1 = new Rectangulos();
        System.out.println(r1.area(8, 4));
        System.out.println(r1.perimetro(8, 4));

    }
}

/**
 * Salida:
 * Construyendo el constructor
 * Hola Joel Desde el constructor
 * Construyendo el constructor
 * Nombre: Joel Alberto
 * Edad: 33 años
 * Construyendo el constructor
 * Nombre: Joel
 * Edad: 33 años
 * Construyendo el constructor
 * Nombre: Alberto
 * Edad: 33 años
 * 3.141592
 * 3.141592
 * 90
 * 90.4
 * 1
 * 1.0999999999999979
 * 3.141592653589793
 * 16.0
 * 10
 * 0
 * 0
 * 32
 * 24
 */
