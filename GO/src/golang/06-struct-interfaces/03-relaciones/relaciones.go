package main

import "fmt"

/*
RELACIÓN DE UNO A UNO
En una relación de uno a uno, un registro en una tabla está relacionado con exactamente un registro en otra tabla. En Go, se puede implementar la relación de uno a uno utilizando la composición de estructuras o tipos de datos. La relación de uno a uno se establece mediante la asignación de una instancia de una estructura a un campo en otra estructura.
*/

type User struct {
	nombre string
	email  string
	activo bool
}

type Student struct {
	user   User // Relación en la que un estudiante solo puede tener un usuario
	codigo string
}

/*
RELACIÓN DE UNO A MUCHOS
En una relación de uno a muchos, un registro está relacionado con varios registros en otra tabla.
En Go, se puede implementar utilizando la composición de estructuras y slices.
La relación se establece mediante el uso de un campo de tipo slice que contiene múltiples instancias del tipo de datos relacionado.
*/

type Curso struct {
	titulo string
	videos []Video
}

type Video struct {
	titulo string
	curso  Curso
}

func main() {

	// Relación de uno a uno
	joel := User{
		nombre: "Joel",
		email:  "joel@email.com",
		activo: true,
	}
	alberto := User{
		nombre: "Alberto",
		email:  "alberto@email.com",
		activo: true,
	}
	joelStudent := Student{
		user:   joel,
		codigo: "900316",
	}
	albertoStudent := Student{
		user:   alberto,
		codigo: "76141",
	}
	fmt.Println()
	fmt.Println(joel)
	fmt.Println(joelStudent)
	fmt.Println()
	fmt.Println(alberto)
	fmt.Println(albertoStudent.user.nombre)
	/*
		Salida:
		{Joel joel@email.com true}
		{{Joel joel@email.com true} 900316}

		{Alberto alberto@email.com true}
		Alberto
	*/

	// Relación de uno a muchos
	video1 := Video{titulo: "01-Introducción"}
	video2 := Video{titulo: "02-Instalación"}

	curso := Curso{
		titulo: "Curso de GO",
		videos: []Video{video1, video2},
	}

	video1.curso = curso
	video2.curso = curso

	fmt.Println()
	fmt.Println(video1.curso.titulo)
	for _, video := range curso.videos {
		fmt.Println(video.titulo)
	}
	/*
		Salida:
		Curso de GO
		01-Introducción
		02-Instalación
	*/

}
