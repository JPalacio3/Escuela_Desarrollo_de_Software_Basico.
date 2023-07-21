package figuras

import (
	"fmt"
)

type Geometria interface {
	area() float64
	perimetro() float64
}

// Función que se asocia a la interface (Reutilizable para cada tipo de figura)
func Medidas(g Geometria) {
	fmt.Println()
	fmt.Println("Para una medida de: ", g)
	fmt.Println()
	fmt.Println("El área es: ", g.area())
	fmt.Println("El perímetro es: ", g.perimetro())

}
