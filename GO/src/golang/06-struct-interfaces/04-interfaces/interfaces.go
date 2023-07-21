package main

import "fmt"

/*
INTERFACES
Las interfaces en Go definen un conjunto de métodos que deben ser implementados por un tipo.
Un tipo puede implementar una interfaz al proporcionar las implementaciones de los métodos requeridos.
Las interfaces permiten lograr la abstracción y el polimorfismo en Go.
Pueden usarse como tipos de datos en funciones y estructuras para aceptar múltiples tipos.
Ayudan a escribir código más genérico y flexible al trabajar con diferentes implementaciones de una funcionalidad común.
*/
type Animal interface {
	mover() string
}

type Perro struct{}
type Pez struct{}
type Pajaro struct{}

func (*Perro) mover() string {
	return "Soy perro y camino"
}

func (*Pez) mover() string {
	return "Soy pez y nado"
}

func (*Pajaro) mover() string {
	return "Soy pájaro y vuelo"
}

func moverAnimal(animal Animal) {
	fmt.Println(animal.mover())
}

func main() {
	perro := Perro{}
	moverAnimal(&perro)

	pez := Pez{}
	moverAnimal(&pez)

	pajaro := Pajaro{}
	moverAnimal(&pajaro)
}

/*
Soy perro y camino
Soy pez y nado
Soy pájaro y vuelo
*/
