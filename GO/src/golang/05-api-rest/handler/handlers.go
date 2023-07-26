package handlers

import (
	"api-rest/db"
	"api-rest/models"
	"encoding/json"
	"fmt"
	"net/http"
)

// Handler para obtener todos los usuarios
func GetUsers(rw http.ResponseWriter, r *http.Request) {
	// fmt.Fprintln(rw, "Lista todos los usuarios")

	// Establecer el encabezado Content-Type en la respuesta como application/json para convertir los datos recibidos de texto a formato json
	rw.Header().Set("Content-type", "application/json")
	// Recibir respuestas de tipo xml
	// rw.Header().Set("Content-type", "text/xml")

	// Realizar la conexión a la base de datos
	db.Connect()

	// Obtener la lista de todos los usuarios desde el modelo
	users := models.ListUsers()

	// Cerrar la conexión a la base de datos
	db.Close()

	// Convertir la lista de usuarios en formato JSON
	output, _ := json.Marshal(users)

	// Convertir la lista de usuarios en formato xml
	// output, _ := xml.Marshal(users)

	// Escribir la respuesta JSON en el ResponseWriter
	fmt.Fprintln(rw, string(output))
}

// Handler para obtener un único usuario
func GetUser(rw http.ResponseWriter, r *http.Request) {
	fmt.Fprintln(rw, "Obtiene un único usuario")
}

// Handler para crear un  usuario
func CreateUser(rw http.ResponseWriter, r *http.Request) {
	fmt.Fprintln(rw, "Permite crear un usuario")
}

// Handler para eliminar un  usuario
func DeleteUser(rw http.ResponseWriter, r *http.Request) {
	fmt.Fprintln(rw, "Permite eliminar un usuario")
}

// Handler para actualizar un  usuario
func UpdateUser(rw http.ResponseWriter, r *http.Request) {
	fmt.Fprintln(rw, "Permite crear un usuario")
}
