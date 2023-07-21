package main

import "fmt"

func main() {
	var nombre1 string
	nombre1 = "Joel"

	var nombre2 string = "Alberto"

	edad := 33

	fmt.Println(nombre1, nombre2, edad)

	// Otras variables

	// Si no se asignan valores, las variables tendrán valores por defecto
	var a int  // 0
	var b float64 // 0
	var c string // ""
	var d bool // false

	fmt.Println(a,b,c,d)
	// Salida:
	// 0 0 "" false


	const pi = 3.1416
	fmt.Println(pi)

}
