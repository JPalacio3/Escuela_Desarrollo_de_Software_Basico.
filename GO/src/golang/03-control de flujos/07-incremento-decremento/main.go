package main

import "fmt"

func main() {
	b := 0

	// Operador de incremento
	b++
	fmt.Println(b) // 1
	b++
	b++
	b++
	b++
	b++
	fmt.Println(b) // 6

	// Operador de decremento

	b--
	fmt.Println(b) // 5
	b--
	b--
	b--
	fmt.Println(b) // 2
}
