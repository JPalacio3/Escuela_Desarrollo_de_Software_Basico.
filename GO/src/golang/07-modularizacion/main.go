package main

import (
	"paquetes/figuras"

	"github.com/donvito/hellomod"
)

func main() {
	// "paquetes/figuras"
	// mensajes.Hola()
	// mensajes.Imprimir()

	// Paquete figuras
	/*
		cua1 := figuras.Cuadrado{Lado: 8}
		figuras.Medidas(&cua1)

		cir1 := figuras.Circulo{Radio: 8}
		figuras.Medidas(&cir1)
	*/

	// Paquete Persona
	/*
		p1 := models.Persona{}
		p1.Constructor("JOEL", 36)
		fmt.Println(p1)

		// Obtener el valor del nombre con el método GET
		fmt.Println(p1.GetNombre())
		// Obtener el vaor de la edad con el método SET
		fmt.Println(p1.GetEdad())

		// Modificar el valor del nombre con el método SET
		p1.SetNombre("Alberto")
		fmt.Println(p1.GetNombre())

		// Modificar el valor de la edad con el método SET
		p1.SetEdad(33)
		fmt.Println(p1.GetEdad())

		fmt.Println(p1)
	*/

	// Paquete GoMod importado de tercero
	hellomod.SayHello() // Hello World v1.0.1!!!

	cua1 := figuras.Cuadrado{Lado: 10}
	figuras.Medidas(&cua1)

}
