package main

import "fmt"

// VARIABLE GLOBAL
/*
Las variables globales en Go son variables declaradas fuera de cualquier función o bloque de código. Tienen alcance en todo el paquete y pueden ser accedidas y modificadas desde cualquier parte del mismo. Se recomienda su uso cuidadoso para evitar colisiones de nombres y acoplamiento excesivo.
*/
var mensaje string

func funcion1() {
	mensaje = "Hola desde la función uno!"
	fmt.Println(mensaje)
}

func funcion2() {
	mensaje = "Hola desde la función dos!"
	fmt.Println(mensaje)
}

func funcion3() {
	mensaje = "Hola desde la función tres!"
	fmt.Println(mensaje)
}

func main() {
	mensaje = "Hola desde la función principal"
	fmt.Println(mensaje)

	defer funcion1()
	funcion2()
	funcion3()
	fmt.Println(mensaje)
}

/*
Salida:
Hola desde la función principal
Hola desde la función dos!
Hola desde la función tres!
Hola desde la función tres!
Hola desde la función uno!

*/
