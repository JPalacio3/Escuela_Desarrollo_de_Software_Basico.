package main

import (
	"fmt"
	"os"
)

func main() {

	// Función Recover
	defer func() {
		if error := recover(); error != nil {
			fmt.Println(("Ups, al parecer el programa no finalizó de manera correcta"))
		}
	}()

	if file, error := os.Open("hoa.txt"); error != nil {
		panic("No fue posible obtener este archivo !!")
	} else {

		// Función anónima que se encarga de mandar al final de la ejecución, la instrucción para cerrar el archivo
		defer func() {
			fmt.Println("Cerrando el archivo")
			file.Close()
		}()

		contenido := make([]byte, 254)
		long, _ := file.Read(contenido)
		contenidoArchivo := string(contenido[:long])
		fmt.Println(contenidoArchivo)
	}
}

/*
Salida:
Hola desde el archivo hola.txt
Estamos en el curso de GO
Cerrando el archivo
*/
