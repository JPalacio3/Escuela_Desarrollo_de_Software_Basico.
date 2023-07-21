package main

import "fmt"

// Función que recibe paámetros
func saludar(nombre string) {
	// fmt.Println("Hola Mundo")
	fmt.Println("Hola", nombre)
}

// Función qu retorna valores:
// Es importante que se debe indicar el tipo de dato que se va a retornar al ejecutarse la función
func sumar(a, b int) int {
	return a + b
}

// Dentro de la función principal debemos invocar la función para que se ejecute
func main() {
	saludar("Joel")
	r := sumar(5, 4)              // Esta ejecución los retorna pero no los imprime, se asigna a una variable para imprimirlo
	fmt.Println("La suma es:", r) // Esta función si los imprime
}
