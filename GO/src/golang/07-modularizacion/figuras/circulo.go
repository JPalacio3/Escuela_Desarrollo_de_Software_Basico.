package figuras

import (
	"math"
)

// Circulo
type Circulo struct {
	Radio float64
}

// Área de Circulo
func (cir *Circulo) area() float64 {
	return math.Pi * (cir.Radio * cir.Radio)
}

// Perímetro del Círculo
func (cir *Circulo) perimetro() float64 {
	return 2 * math.Pi * cir.Radio
}
