package main

import "fmt"

func main() {
	hola := "Hola"
	mundo := "Mundo"

	fmt.Print(hola)
	fmt.Print(mundo)

	fmt.Println(hola)
	fmt.Println(mundo)

	nombre:= "Joel"
	edad := 33

	// Verbos de formato:
	/*
	%s se utiliza para indicar que será imprimido un valor string
	%d se utiliza para indicar que será imprimido un valor entero
	%v se utiliza cuando se desconozca el tipo de dato que será imprimido
	%T se utiliza qué tipo de dato almacena una variable
	*/
	fmt.Printf("Hola, %s y su edad es %d \n", nombre, edad)
	fmt.Printf("Hola, %v y su edad es %v \n", nombre, edad)

	mensaje := fmt.Sprintf("Hola, %s y su edad es %d", nombre, edad)
	fmt.Println(mensaje)

	fmt.Printf("nombre:  %T \n", nombre)
	fmt.Printf("edad:  %T \n", edad)

	// Ingresar datos por teclado
	fmt.Print(" Ingrese otro nombre :  ")
	fmt.Scanln(&nombre)

	fmt.Println("Segundo nombre :", nombre)
}
