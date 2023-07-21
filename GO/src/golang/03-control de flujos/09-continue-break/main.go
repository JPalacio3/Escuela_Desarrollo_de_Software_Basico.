package main

import "fmt"

func main() {
	// ciclo que imprime los núemros del 1 al 10
	for i := 0; i <= 10; i++ {

		if i == 5 {
			fmt.Println("Saltar el bucle en la quinta ejecución")
			continue // Hace un salto hacia la siguiente ejecución en un punto determinado
		}

		if i == 8 {
			fmt.Println("Romper con el bucle en la octava ejecución")
			break // Rompe la ejecución del bucle en un punto determinado
		}

		fmt.Println(i)
	}

}
