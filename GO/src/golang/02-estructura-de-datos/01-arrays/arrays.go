package main

import "fmt"

func main() {
	// arrays: Se declara la cantidad de elementos que contendrá dentro de las llaves y el tipo de dato que contendrá
	var numeros [5]int
	fmt.Println(numeros)

	// Modificar valores mediante el índice, comenzando en 0 para el primer elemento
	numeros[0] = 10
	numeros[1] = 20
	numeros[2] = 30
	fmt.Println(numeros)

	// Imprimir el valor de un determinado objeto mediante el índice
	fmt.Println(numeros[2])

	// Arrays con valores
	nombres := [3]string{"Joel", "Alberto", "Palacio"}
	fmt.Println(nombres)

	// Definir un arreglo sin colocarle la longitud
	colores := [...]string{
		"rojo",
		"verde",
		"negro",
		"azul",
	}
	// Añadiendo la función len podemos saber la longitud que tiene el arreglo
	fmt.Println(colores, len(colores))

	// Definir los índices de los objetos
	monedas := [...]string{
		0: "Dolar",
		2: "Soles",
		3: "Pesos",
		5: "Oro",
	}
	fmt.Println(monedas, len(monedas))

	// Subarreglo : Cuando es desde el inicio no es necesario poner  0
	subMoneda := monedas[:3]
	fmt.Println(subMoneda, len(subMoneda))
	// Cuando s a partir de cierto punto hasta el final, no es necesario poner el índice final
	subMoneda2 := monedas[3:]
	fmt.Println(subMoneda2, len(subMoneda2))

}

/*
Salida:
λ go run arrays.go

[0 0 0 0 0]
[10 20 30 0 0]
30
[Joel Alberto Palacio]
[rojo verde negro azul] 4
[Dolar  Soles Pesos  Oro] 6
[Dolar  Soles] 3
[Pesos  Oro] 3
*/
