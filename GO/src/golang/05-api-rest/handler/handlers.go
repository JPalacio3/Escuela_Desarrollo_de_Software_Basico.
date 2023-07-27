package handlers

import (
	"api-rest/db"
	"api-rest/models"
	"encoding/json"
	"fmt"
	"net/http"
	"strconv"

	"github.com/gorilla/mux"
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
	// fmt.Fprintln(rw, "Lista todos los usuarios")
	rw.Header().Set("Content-type", "application/json")

	// Obteber id
	vars := mux.Vars(r) // Obtenemos un mapa de las variables de la URL registradas en el router.
	/*
	   Obtenemos el valor de la variable "id" del mapa de variables.
	   Esta variable contiene el valor de "id" en formato de cadena (string).
	   Utilizamos strconv.Atoi() para convertir el valor a un número entero (int).
	   El guión bajo "_" se utiliza para ignorar el segundo valor de retorno (el error).
	*/
	userId, _ := strconv.Atoi(vars["id"])
	db.Connect()
	user := models.GetUser(userId)
	db.Close()
	output, _ := json.Marshal(user)
	fmt.Fprintln(rw, string(output))
}

// Handler para crear un  usuario
func CreateUser(rw http.ResponseWriter, r *http.Request) {
	// fmt.Fprintln(rw, "Permite crear un usuario")
	rw.Header().Set("Content-type", "application/json")
	// Obteber Todo el registro
	user := models.User{}
	decoder := json.NewDecoder(r.Body)

	if err := decoder.Decode(&user); err != nil {
		fmt.Fprintln(rw, http.StatusUnprocessableEntity)
	} else {
		db.Connect()

		user.Save()

		db.Close()
	}

	output, _ := json.Marshal(user)
	fmt.Fprintln(rw, string(output))

}

// Handler para eliminar un  usuario
func DeleteUser(rw http.ResponseWriter, r *http.Request) {
	// fmt.Fprintln(rw, "Lista todos los usuarios")
	rw.Header().Set("Content-type", "application/json")
	// Obteber id
	vars := mux.Vars(r) // Obtenemos un mapa de las variables de la URL registradas en el router.
	userId, _ := strconv.Atoi(vars["id"])
	db.Connect()

	user := models.GetUser(userId)
	user.Delete()

	db.Close()
	output, _ := json.Marshal(user)
	fmt.Fprintln(rw, string(output))
}

// Handler para actualizar un  usuario
func UpdateUser(rw http.ResponseWriter, r *http.Request) {
	// fmt.Fprintln(rw, "Permite crear un usuario")
	rw.Header().Set("Content-type", "application/json")
	// Obteber Todo el registro
	user := models.User{}
	decoder := json.NewDecoder(r.Body)

	if err := decoder.Decode(&user); err != nil {
		fmt.Fprintln(rw, http.StatusUnprocessableEntity)
	} else {
		db.Connect()

		user.Save()

		db.Close()
	}
}
