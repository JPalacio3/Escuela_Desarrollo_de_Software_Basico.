package main

import (
	"fmt"
	"strings"
)

/*
FUNCIONES ANÓNIMAS:
Las funciones anónimas en Go son funciones sin nombre que se pueden crear y utilizar en el lugar donde se necesitan. Se pueden asignar a variables o utilizar como argumentos de otras funciones. Son útiles para encapsular lógica y pueden acceder a variables locales y capturar variables del ámbito en el que se definen.
*/

// Closures: Es una función que retorna otra función, como una función anidada dentro de otra función
func repeat(n int) func(cadena string) string {

	return func(cadena string) string {
		return strings.Repeat(cadena, n)
	}
}

func main() {

	// Función anónima
	func() {
		fmt.Println("Hola desde la función anónima")
	}() // Salida: Hola desde la función anónima

	myfunc := func(nombre string) string {
		return fmt.Sprintf("Hola, %s desde la segunda función anónima", nombre)
	}
	fmt.Println(myfunc("Joel")) // Hola Joel desde la segunda función anónima

	// Función Closur
	repeat3 := repeat(3)
	fmt.Println(repeat3(" Hola "))  // Hola Hola Hola
	fmt.Println(repeat3(" Mundo ")) // Mundo  Mundo  Mundo
	repeat5 := repeat(5)
	fmt.Println(repeat5(" Joel")) //  Joel Joel Joel Joel Joel

}
