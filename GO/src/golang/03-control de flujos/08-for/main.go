package main

import "fmt"

func main() {

	// Bucle for
	for i := 0; i <= 100; i++ {
		if i%2 == 0 {
			fmt.Println(i)
		} // Imprime lso números pares del 1 a 100
	}

	// Bucle tipo while
	numeros := 124555
	c := 0
	for numeros > 0 {
		numeros /= 10
		c++
	}
	fmt.Println(" Cantidad de dígitos es:", c) //  Cantidad de dígitos es: 6

	// Bucle infinito
	/*
		for {
			fmt.Println(" Hola Mundo")
		} // Imprime "Hola Mundo " INFINITAS VECES
	*/
}
