package main

import "fmt"

// Estruct persona
type Persona struct {
	nombre string
	edad   int
}

// Métodos
func (p *Persona) imprimir() {
	fmt.Printf("Nombre: %s \n Edad: %d \n", p.nombre, p.edad)
}

func (p *Persona) editNombre(nuevoNombre string) {
	p.nombre = nuevoNombre
}

// Herencia
type Empleado struct {
	Persona
	sueldo float64
}

func main() {
	// Accedemos a la estructura y asignamos valores para imprimir
	p1 := Persona{"Joel", 33}
	// fmt.Println(p1)
	p1.imprimir()

	// Accedemos al valor del atributo y lo modificamos
	// p1.nombre = "Alberto"
	// fmt.Println(p1)
	p1.editNombre("Alberto")
	p1.imprimir()

	p2 := Persona{
		nombre: "Joel",
		edad:   33,
	}
	// fmt.Println(p2)
	p2.imprimir()

	em1 := Empleado{
		sueldo: 500,
	}
	em1.nombre = "Palacio"
	em1.edad = 30
	em1.imprimir()
	fmt.Println(em1) // {{Palacio 30} 500}

}
