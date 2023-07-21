package main

import "fmt"

func main() {
	a := 20.0
	b := 10.0

	// Suma
	result := a + b
	fmt.Println("Suma: ", result)

	// Resta
	result = a-b
	fmt.Println("Resta: ", result)

	// Multiplicación
	result = a*b
	fmt.Println("Multiplicación: ", result)

	// División
	result = a / b
	fmt.Println("División: ", result)

	// División decimal
	var divi float64 = b / a
	fmt.Println("División: ", divi)

	// Modulo de una división
	result = 3 % 2
	fmt.Println("Módulo: ", result)

}
