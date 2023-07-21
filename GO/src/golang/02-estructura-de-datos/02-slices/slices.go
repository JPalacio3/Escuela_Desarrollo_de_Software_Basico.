package main

import "fmt"

func main() {
	// Slices: A diferencia de los arrays, los slices no tienen definido dentro de las llaves la cantidad de elementos que contendrá
	numeros := []int{1, 2, 3}
	fmt.Println(numeros, len(numeros))

	// Agregar elementos al slice
	numeros = append(numeros, 4, 5, 6)
	fmt.Println(numeros, len(numeros))

	// SubSlice
	subNumeros := numeros[:2]
	numeros[0] = 100
	fmt.Println(numeros, len(numeros))
	fmt.Println(subNumeros, len(subNumeros))

	// Punteros: Es para saber en dónde inicia y en donde termina el slice
	// Longitud:  cantidad actual de elementos almacenados en el slice
	// Capacidad: antidad máxima de elementos que el slice puede contener antes de que se necesite asignar más memoria.

	meses := []string{"Enero", " Febrero", " Marzo"}
	fmt.Printf("Len: %v, Cap: %v, %p \n", len(meses), cap(meses), meses)
	// Salida:  Len: 3, Cap: 3, 0xc000076510

	//Agregar un elemento al slice
	meses = append(meses, "Abril")
	fmt.Printf("Len: %v, Cap: %v, %p \n", len(meses), cap(meses), meses)
	// Salida: Len: 4, Cap: 6, 0xc00005e060
}
