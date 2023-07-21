package figuras

/*
Práctica realizado con Interfaces ahora modulariza
Crear un nuevo paquete figuras

Luego separa la estructura de cuadrado con sus métodos en otro archivo

Luego separa la estructura de circulo con sus métodos  en otro archivo

Luego el interfaces con su función mediadas  en otro archivo

Importa desde la main.go para crear la estructura y ver las medidas
*/

// Cuadrado
type Cuadrado struct {
	Lado float64
}

// Área de Cuadrado
func (cua *Cuadrado) area() float64 {
	return cua.Lado * cua.Lado
}

// Perímetro de Cuadrado
func (cua *Cuadrado) perimetro() float64 {
	return 4 * cua.Lado
}
