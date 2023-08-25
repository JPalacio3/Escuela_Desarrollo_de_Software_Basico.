package test;

import herencia.*;

public class TestHerencia {
    public static void main(String[] args) {
        Empleados empleado1 = new Empleados("Joel", 19000);
        System.out.println(empleado1);

        Empleados empleado2 = new Empleados("Alberto", 6000);
        System.out.println(empleado2);

        Empleados empleado3 = new Empleados("Palacio", 10000);
        System.out.println(empleado3);
    }
}
