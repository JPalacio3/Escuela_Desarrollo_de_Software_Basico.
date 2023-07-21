package main

import (
	"fmt"
	"math"
)

/*
PRÁCTICA: Uso de Interfaces.
En esta práctica vamos a sacar área y perímetro de un cuadrado y círculo utilizando interfaces.

Cuadrado
área = ancho * altura
perimetro = 2*ancho + 2*altura

Círculo
área = pi * (radio * radio)
perimetro = 2*pi * radio
*/

// Interface: Se asignan a la interface los dos métodos similares
type Geometrica interface {
	area() float64
	perimetro() float64
}

// Cuadrado
type Cuadrado struct {
	lado float64
}

// Circulo
type Circulo struct {
	radio float64
}

// Área de Cuadrado
func (cua *Cuadrado) area() float64 {
	return cua.lado * cua.lado
}

// Perímetro de Cuadrado
func (cua *Cuadrado) perimetro() float64 {
	return 4 * cua.lado
}

// Área de Circulo
func (cir *Circulo) area() float64 {
	return math.Pi * (cir.radio * cir.radio)
}

// Perímetro del Círculo
func (cir *Circulo) perimetro() float64 {
	return 2 * math.Pi * cir.radio
}

// Función que se asocia a la interface (Reutilizable para cada tipo de figura)
func medidas(g Geometrica) {
	fmt.Println()
	fmt.Println("Para una medida de: ", g)
	fmt.Println()
	fmt.Println("El área es: ", g.area())
	fmt.Println("El perímetro es: ", g.perimetro())

}

func main() {
	cuad := Cuadrado{lado: 4}
	circ := Circulo{radio: 5}

	medidas(&cuad)
	medidas(&circ)
}

/*
Salida:
Para una medida de:  &{4}

El área es:  16
El perímetro es:  16

Para una medida de:  &{5}

El área es:  78.53981633974483
El perímetro es:  31.41592653589793
*/
