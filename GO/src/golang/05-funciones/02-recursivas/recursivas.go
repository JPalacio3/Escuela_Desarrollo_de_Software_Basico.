package main

import "fmt"

/*
FUNCIONES RECURSIVAS:
Las funciones recursivas son aquellas que se llaman a sí mismas dentro de su propia definición. Se dividen en un caso base que detiene la recursión y un caso recursivo que resuelve subproblemas más pequeños. Deben diseñarse cuidadosamente para evitar bucles infinitos y pueden ser útiles para resolver problemas complejos de manera elegante.
*/

func factorial(n int) int {
	if n == 0 {
		return 1 // Caso base: factorial de 0 es 1
	}

	f := n * factorial(n-1) // Caso recursivo: n multiplicado por factorial de n-1

	return f
}

func main() {
	fmt.Println(factorial(3)) // Salida: 6
	fmt.Println(factorial(5)) // Salida: 120
}
