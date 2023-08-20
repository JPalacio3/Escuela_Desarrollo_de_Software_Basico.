package test;

import encapsulamiento.*;

public class TestPersona {
    public static void main(String[] args) {

        Persona persona1 = new Persona("Joel", 33, false);
        System.out.println(persona1.getNombre());
        System.out.println(persona1.getEdad());
        System.out.println(persona1.isEliminado());
        String estado = persona1.toString();
        System.out.println(estado);

        persona1.setNombre("Alberto");
        System.out.println(persona1.getNombre());
        persona1.setEdad(30);
        System.out.println(persona1.getEdad());
        persona1.setEliminado(true);
        System.out.println(persona1.isEliminado());

        System.out.println(persona1);
        System.out.println(estado);

    }
}
