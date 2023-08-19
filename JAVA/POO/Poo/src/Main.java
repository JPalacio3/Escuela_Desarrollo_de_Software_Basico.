/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */

import clases.Persona;

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
    }
}

/**
 * Salida:
Nombre: Joel
Edad: 33 años
Nombre: Alberto
Edad: 33 años
 */
