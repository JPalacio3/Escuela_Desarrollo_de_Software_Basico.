package models

type Persona struct {
	nombre string
	edad   int
}

func (p *Persona) Constructor(nombre string, edad int) {
	p.nombre = nombre
	p.edad = edad
}

// Obtener el valor de un atributo mediante una función GET
func (p *Persona) GetNombre() string {
	return p.nombre
}

// Modificar el valor de un atributo mediante una función SET
func (p *Persona) SetNombre(nombre string) {
	p.nombre = nombre
}

// Obtener el valor de un atributo mediante una función GET
func (p *Persona) GetEdad() int {
	return p.edad
}

// Modificar el valor de un atributo mediante una función SET
func (p *Persona) SetEdad(edad int) {
	p.edad = edad
}
