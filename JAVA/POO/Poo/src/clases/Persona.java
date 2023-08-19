package clases; // Las clases creadas dentro de paquetes, deben definirse usando el nombre de ese paquete

public class Persona {
    public String nombre;
    public int edad;

    /**
     * @autor Jpalacio
     * @param Este método permite mostrar los datos de nombre y edad de una persona
     */
    public void mostrarDatos() {
        System.out.println("Nombre: " + nombre);
        System.out.println("Edad: " + edad + " años");
    }
}
