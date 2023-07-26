package main

import (
	"go-mysql/db"
	"go-mysql/models"
)

func main() {
	db.Connect()
	db.CreateTable(models.UserSchema)
	db.Ping()
	db.Close()
}
