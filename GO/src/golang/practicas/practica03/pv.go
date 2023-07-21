package main

import "fmt"

/*
Practica 03: Calcular el Precio de Venta
Enunciado: dado el valor de venta de productos, hallar el IGV (18%) y el precio de venta.

Análisis: para la solución de este problema, se requiere que el usuario ingrese el valor de venta del producto y el sistema realice el cálculo respectivo para hallar el IGV y el precio de venta.
*/

//Función que calcula el igv
func calcularIgv(vv, igv float64) float64 {
	return igv * vv
}

//Funcion que calcula percio de venta
func precioVenta(vv, igv float64) float64 {
	return vv + igv
}

//Función principal
func main() {

	//Variables
	var vv, igv, pv float64

	//Entrada  de datos
	fmt.Print("Ingrese Valor de Venta: ")
	fmt.Scanln(&vv)

	//Calcular igv
	igv = calcularIgv(vv, 0.18)

	//Calcular precio de venta
	pv = precioVenta(vv, igv)

	//Salida de datos
	fmt.Println("==========================")
	fmt.Println("Valor de Venta:", vv, "MXN")
	fmt.Println("IGV:", igv, "MXN")
	fmt.Println("Precio de Venta:", pv, "MXN")
	fmt.Println("==========================")
}
