package main

import "fmt"

/*
Practica 01: Suma de dos números enteros
Enunciado: dado dos números enteros, hallar la suma.

Análisis: para la solución de este problema, se requiere que el usuario ingrese dos números enteros y el sistema realice el cálculo respectivo para hallar la suma.

*/

func datos() int {
	var a, b int

	fmt.Print("Ingrese un número a continuación :")
	fmt.Scanln(&a)
	fmt.Print("Ingrese otro número a continuación :")
	fmt.Scanln(&b)

	return a + b

}

func main() {
	r := datos()

	fmt.Println("La suma es", r)
}
