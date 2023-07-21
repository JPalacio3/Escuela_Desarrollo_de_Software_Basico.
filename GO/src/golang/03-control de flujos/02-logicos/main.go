package main

import "fmt"

func main() {

	// Not: Este operador se usa para negar un valor bool
	fmt.Println(!true)
	// Salida : false
	fmt.Println(!false)
	// Salida: true

	// And: Compara dos valores y ambas debn sr postivo para que devuelva positiva
	fmt.Println(true && true)
	// Salida: true
	fmt.Println(false && true)
	// Salida: false
	fmt.Println(false && false)
	// Salida: false

	// Or: Si una de las dos condiciones es positiva, devuelve positivo
	fmt.Println(true || true)
	// Salida: true
	fmt.Println(true || false)
	// Salida: true
	fmt.Println(false || true)
	// Salida: true
	fmt.Println(false || false)
	// Salida: false

	b := 2
	r := b == 2 && 4 > b
	fmt.Println(r)
	// Salida: true

	z := b == 2 && !(4 > b)
	fmt.Println(z)
	// Salida: false

	y := b == 2 || 4 > b
	fmt.Println(y)
	// Salida: true

	x := b == 2 || !(4 > b)
	fmt.Println(x)
	// Salida: true

}
