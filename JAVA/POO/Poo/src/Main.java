/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */

import clases.Calculadora;
import clases.Persona;
import static java.lang.Math.*;

/**
 *
 * @author JPalacio
 */
public class Main {

    public static void main(String[] args) {

        Persona persona1; // Creamos un objeto nuevo instanciado de la clase
        persona1 = new Persona(); // Asignamos el objeto a la clase padre, indicando que es una nueva instancia
        persona1.nombre = "Joel"; // Asignamos los valores de los atributos que contiene la clase
        persona1.edad = 33;
        persona1.mostrarDatos(); // Invocamos el método que contiene la clase para ejecutarla

        Persona persona2 = new Persona(); // Instanciamos el objeto de manera directa a la clase
        persona2.nombre = "Alberto";
        persona2.edad = 33;
        persona2.mostrarDatos();

        System.out.println(Calculadora.PI); // Ejecutamos el método PI de la clase calculadora(paquete clases)
        Calculadora.PI = 3.15; // Es posible aceder directamente a modifiar el valor de un objeto
        System.out.println(Calculadora.PI);

        System.out.println(Calculadora.sumar(40, 50)); // Ejecutamos el método sumar de la clase calculadora

        System.out.println(PI); // Importar la clase Math de java completa para usar sus atributos y métodos
        System.out.println(pow(4, 2));
    }
}

/**
 * Salida:
 * Nombre: Joel
 * Edad: 33 años
 * Nombre: Alberto
 * Edad: 33 años
 * 3.141592
 * 3.15
 * 90
 * 3.141592653589793
 * 16.0
 */
