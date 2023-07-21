package main

import "fmt"

func main() {
	var vocal string
	fmt.Print("Ingrese una letra: ")
	fmt.Scanln(&vocal)

	/*
		SIN DECLARAR EN EL SWITCH LA VARIABLE Y SE DECLARA CADA CASO
			switch {
			case vocal == "a" || vocal == "A":
				fmt.Println(vocal, "Es una Vocal")
			case vocal == "e" || vocal == "E":
				fmt.Println(vocal, "Es una Vocal")
			case vocal == "i" || vocal == "I":
				fmt.Println(vocal, "Es una Vocal")
			case vocal == "o" || vocal == "O":
				fmt.Println(vocal, "Es una Vocal")
			case vocal == "u" || vocal == "U":
				fmt.Println(vocal, "Es una Vocal")
			default:
				fmt.Println(vocal, "NO es una Vocal")
			}
	*/

	// SE DECLARA LA VARIABLE EN EL SWITCH PARA EVALUAR MÚLTIPLES CASOS EN UNA SOLA LÍNEA
	switch vocal {
	case "a", "e", "i", "o", "u", "A", "E", "I", "O", "U":
		fmt.Println(vocal, "Es una Vocal")
	default:
		fmt.Println(vocal, "NO es una Vocal")
	}

}
