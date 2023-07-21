package main

import "fmt"

/*
FUNCIONES VARIÁDICAS:
Las funciones variádicas permiten aceptar un número variable de argumentos. Se definen agregando ... después del tipo del último parámetro de la función. Dentro de la función, los argumentos se tratan como un "slice". Son útiles cuando no se sabe cuántos argumentos se pasarán o se desea mayor flexibilidad en la llamada de la función.
*/

func sumar(numeros ...int) int {
	var total int
	for _, num := range numeros {
		total += num
	}
	return total
}

/*
RETORNO DE MÚLTIPLES VALORES
El retorno de múltiples valores en Go permite que una función devuelva más de un valor. Se logra al listar los valores separados por comas en la declaración de retorno de la función. Al llamar a la función, puedes asignar los valores de retorno a variables diferentes.
*/

func suma(nombre string, numeros ...int) (string, int) {
	mensaje := fmt.Sprintf("La suma de %s es:", nombre)
	var total int
	for _, num := range numeros {
		total += num
	}
	return mensaje, total
}

func main() {
	// Función sumar
	result := sumar(4, 5, 8, 6, 50, 70, 50, 2)
	fmt.Println(result)

	// Función suma
	mensaje, resultado := suma("Joel ", 4, 5, 8, 6, 50, 70, 2)
	fmt.Println(mensaje, resultado)

} // Salida: La suma de Joel es:  145
