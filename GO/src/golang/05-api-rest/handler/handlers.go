package handlers

import (
	"api-rest/models"
	"encoding/json"
	"net/http"
	"strconv"

	"github.com/gorilla/mux"
)

// Handler para obtener todos los usuarios
func GetUsers(rw http.ResponseWriter, r *http.Request) {

	if users, err := models.ListUsers(); err != nil {
		models.SendNoFound(rw)
	} else {
		models.SendData(rw, users)
	}

}

// Handler para obtener un único usuario
func GetUser(rw http.ResponseWriter, r *http.Request) {

	if user, err := getUserByRequest(r); err != nil {
		models.SendNoFound(rw)
	} else {
		models.SendData(rw, user)
	}
}

// Handler para crear un  usuario
func CreateUser(rw http.ResponseWriter, r *http.Request) {

	// Obtener el usuario
	user := models.User{}
	decoder := json.NewDecoder(r.Body)

	if err := decoder.Decode(&user); err != nil {
		models.SendUnprocessableEntity(rw)
	} else {
		user.Save()
		models.SendData(rw, user)
	}
}

// Handler para eliminar un  usuario
func DeleteUser(rw http.ResponseWriter, r *http.Request) {

	if user, err := getUserByRequest(r); err != nil {
		models.SendNoFound(rw)
	} else {
		user.Delete()
		models.SendData(rw, user)
	}
}

// Handler para actualizar un  usuario
func UpdateUser(rw http.ResponseWriter, r *http.Request) {

	var userId int64

	// Obteber Todo el registro
	if user, err := getUserByRequest(r); err != nil {
		models.SendNoFound(rw)
	} else {
		userId = user.Id
	}
	user := models.User{}
	decoder := json.NewDecoder(r.Body)

	if err := decoder.Decode(&user); err != nil {
		models.SendUnprocessableEntity(rw)
	} else {
		user.Id = userId
		user.Save()
		models.SendData(rw, user)
	}
}

func getUserByRequest(r *http.Request) (models.User, error) {
	vars := mux.Vars(r) // Obtenemos un mapa de las variables de la URL registradas en el router.
	userId, _ := strconv.Atoi(vars["id"])

	if user, err := models.GetUser(userId); err != nil {
		return *user, err
	} else {
		return *user, nil
	}
}
