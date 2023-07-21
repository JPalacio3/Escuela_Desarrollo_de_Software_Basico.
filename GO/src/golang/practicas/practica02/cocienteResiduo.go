package main

import "fmt"

/*
Practica 02: Calcular cociente y el Residuo de dos números enteros
Enunciado: halar el cociente y el residuo (resto) de dos números enteros.

Análisis: para la solución de este problema, se requiere que el usuario ingrese dos números enteros y el sistema realice el cálculo respectivo para hallar el cociente y residuo.
*/
func cociente() int {
	var a, b int

	// Ingreso de datos
	fmt.Print("\n( COCIENTE ) -> Ingrese un número ENTERO a continuación : ")
	fmt.Scanln(&a)
	fmt.Print("( COCIENTE ) -> Ingrese otro número ENTERO a continuación : ")
	fmt.Scanln(&b)

	// Calcular el cociente
	return a / b
}

func residuo() int {

	var a, b int

	// Ingreso de datos
	fmt.Print("\n\n( RESIDUO ) -> Ingrese un número ENTERO a continuación : ")
	fmt.Scanln(&a)
	fmt.Print("( RESIDUO ) -> Ingrese otro número ENTERO a continuación : ")
	fmt.Scanln(&b)

	// Calcular el residuo
	return a % b
}

func main() {
	c := cociente()
	fmt.Println("\nEl Cociente de los números que ingresó es:", c)

	r := residuo()
	fmt.Println("\nEl residuo de los números que ingresó es:", r)

}
