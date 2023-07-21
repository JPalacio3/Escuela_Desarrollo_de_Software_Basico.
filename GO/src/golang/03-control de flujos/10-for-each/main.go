package main

import "fmt"

func main() {
	nombres := [...]string{"Joel", "Alberto", "Palacio", "Cano"}

	// Recorrer un arreglo al modo for each
	for indice, elemento := range nombres {
		fmt.Println(indice, elemento)
	}
	// Salida: Devuelve los índices y los elementos
	/*
		0 Joel
		1 Alberto
		2 Palacio
		3 Cano
	*/

	for _, elemento := range nombres {
		fmt.Println(elemento)
	}
	// Salida: Devuelve los elementos
	/*
		Joel
		Alberto
		Palacio
		Cano
	*/

	for indice, _ := range nombres {
		fmt.Println(indice)
	}
	// Salida: Devuelve solo los índices
	/*
		0
		1
		2
		3
	*/

	// Recorrer un arreglo de la manera for
	for i := 0; i < len(nombres); i++ {
		fmt.Println(nombres[i])
	}
	// Salida: Devuelve los elementos
	/*
		Joel
		Alberto
		Palacio
		Cano
	*/

}
