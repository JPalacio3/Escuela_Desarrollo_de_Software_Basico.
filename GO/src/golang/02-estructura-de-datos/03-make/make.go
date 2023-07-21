package main

import "fmt"

func main() {
	// Función make

	/* En la función make, primero se asigna el tipo de datos que contndrá el arreglo,
	despues se asigna la longitud inicial que pose el arreglo,
	y el último número corresponde a la capacidad final

	*/
	numeros := make([]int, 4, 5)

	numeros[0] = 100
	numeros[1] = 200
	numeros[2] = 300
	numeros[3] = 400

	fmt.Println(numeros, len(numeros), cap(numeros))
	// [100 200 300 400] 4 5

	numeros = append(numeros, 500)
	fmt.Println(numeros, len(numeros), cap(numeros))
	// [100 200 300 400 500] 5 5

}
