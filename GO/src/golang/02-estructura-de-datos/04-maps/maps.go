package main

import "fmt"

func main() {
	// maps
	dias := make(map[int]string)
	fmt.Println(dias) // map[]

	// Agregar datos
	dias[1] = "lunes"
	dias[2] = "martes"
	dias[3] = "miercoles"
	dias[4] = "jueves"
	dias[5] = "viernes"
	dias[6] = "sabado"
	dias[7] = "domingo"
	fmt.Println(dias) // map[1:lunes 2:martes 3:miercoles 4:jueves 5:viernes 6:sabado 7:domingo]

	// Modificar datos
	dias[2] = "Febrero"
	fmt.Println(dias) // map[1:lunes 2:Febrero 3:miercoles 4:jueves 5:viernes 6:sabado 7:domingo]

	// Si indicamos una clave que no existe, se crea un nuevo elemento
	dias[8] = "martes"
	fmt.Println(dias) // map[1:lunes 2:Febrero 3:miercoles 4:jueves 5:viernes 6:sabado 7:domingo 8:martes]

	// Eliminar un elemento
	delete(dias, 8)
	fmt.Println(dias) // map[1:lunes 2:Febrero 3:miercoles 4:jueves 5:viernes 6:sabado 7:domingo]

	// Conocer la extensión del mapa, pero la capacidad como es variable no se puede conocer
	fmt.Println(dias, len(dias)) // map[1:lunes 2:Febrero 3:miercoles 4:jueves 5:viernes 6:sabado 7:domingo] 7

	// Nuevo map: se puede indicar que los valores sean arreglos
	estudiantes := make(map[string][]int)

	// Agregar elementos de tipo arreglo: los mapas pueden contener cualquier tipo de estructura de dato dentro suyo
	estudiantes["Joel"] = []int{13, 15, 16}
	estudiantes["Alberto"] = []int{17, 18, 19}
	fmt.Println(estudiantes) // map[Alberto:[17 18 19] Joel:[13 15 16]]

	// Acceder a un elemento
	fmt.Println(estudiantes["Joel"]) // [13 15 16]

	// Acceder a un valor específico del elemento
	fmt.Println(estudiantes["Joel"][1]) // 15

}
