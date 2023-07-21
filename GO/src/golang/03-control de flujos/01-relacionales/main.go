package main

import "fmt"

// Relacionales o comparadores
func main() {
	a := 4
	b := 5

	var r bool

	// Igualdad
	r = a == b
	fmt.Printf("%d es igual que %d ? %t \n", a, b, r)
	// Salida: 4 es igual que 5 ? false

	// Distinto
	r = a != b
	fmt.Printf("%d es distinto que %d ? %t \n", a, b, r)
	// Salida: 4 es distinto que 5 ? true

	//  Mayor que
	r = a > b
	fmt.Printf("%d es mayor que %d ? %t \n", a, b, r)
	// Salida: 4 es mayor que 5 ? false

	// Menor que
	r = a < b
	fmt.Printf("%d es menor que %d ? %t \n", a, b, r)
	// Salida: 4 es menor que 5 ? true

	// Mayor o Igual que
	r = a >= b
	fmt.Printf("%d es mayor o igual que %d ? %t \n", a, b, r)
	// Salida: 4 es mayor o igual que 5 ? false

	// Menor o Igual que
	r = a <= b
	fmt.Printf("%d es menor o igual que %d ? %t \n", a, b, r)
	// Salida: 4 es menor o igual que 5 ? true

}
