package mensajes

import "fmt"

// Cuando se nombra la función con la primer letra en mayúscula esa función es pública
// Si la primera letra de la función es solamente es minúscula, esa función es privada
func Hola() {
	fmt.Println("Hola desde el paquete Mensaje")
}

const mensaje = "Hola desde mi constante"

func Imprimir() {
	fmt.Println(mensaje)
	privada()
}

func privada() {
	fmt.Println("Hola desde mi función privada")
}
