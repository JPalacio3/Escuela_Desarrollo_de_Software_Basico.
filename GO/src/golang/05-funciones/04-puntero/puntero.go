package main

import "fmt"

/*
PUNTEROS:
En relación a los punteros en Go, son variables especiales que almacenan la dirección de memoria de otro valor en lugar del valor en sí mismo. Se utilizan con el operador * antes del tipo de dato para declarar un puntero y el operador & para obtener la dirección de memoria de una variable existente. Para acceder al valor al que apunta un puntero, se utiliza el operador *.
*/

func modificaValor(cadena *string) {
	fmt.Printf("%p\n", cadena)
	*cadena = "Hola desde la función"
}

func main() {
	cadena := "Hola desde GO"
	fmt.Printf("%p\n", &cadena)
	fmt.Println("Antes de la función: ", cadena)

	modificaValor(&cadena) // Referencia de la memoria

	fmt.Println("Despues de la función: ", cadena)
}
// Salida:
/*
0xc000052270
Antes de la función:  Hola desde GO
0xc000052270
Despues de la función:  Hola desde la función
*/
