package main

import (
	"fmt"
	"go-mysql/db"
	"go-mysql/models"
)

func main() {
	db.Connect()
	// fmt.Println(db.ExistTable("users"))
	// db.CreateTable(models.UserSchema, "users")
	// db.Ping()

	user := models.CreateUser("Alberto", "Joel123", "Joelpalaio630@gmail.com")
	// user := models.ListUsers()
	// fmt.Println(users)

	// user := models.GetUser(2)
	fmt.Println(user)
	// user.Username = "Joelito"
	// user.Password = "1001020823"
	// user.Email = "Joel@gmail.com"
	// user.Save()
	// user.Delete()
	// db.TrancateTable("users")
	fmt.Println(models.ListUsers())

	// fmt.Println(user)
	db.Close()
}
