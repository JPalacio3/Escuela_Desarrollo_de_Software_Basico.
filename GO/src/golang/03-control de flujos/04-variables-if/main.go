package main

import "fmt"

func main() {
	if nombre, edad := "Alberto", 33; nombre == "Joel" {
		fmt.Println("Hola, ", nombre)
	} else {
		fmt.Printf("Nombre: %s - Edad: %d\n", nombre, edad)
	}

	// Obtener valor de un mapa
	users := make(map[string]string)

	users["Joel"] = "Joel@gmail.com"
	users["Alberto"] = "Alberto@gmail.com"

	if correo, ok := users["Palacio"]; ok {
		fmt.Println(correo, ok)
	} else {
		fmt.Println("No fue posible obtener el valor")
	}
	// Salida: No fue posible obtener el valor

}
