package db

import (
	"database/sql"
	"fmt"

	_ "github.com/go-sql-driver/mysql"
)

// username:password:contraseña@tcp(localhost:3306)/database

const url = "root:root@tcp(localhost:3306)/goweb_db"

// Guarda la conexión
var db *sql.DB

// Realiza la conexión
func Connect() {
	connection, err := sql.Open("mysql", url)
	if err != nil {
		panic(err)
	}
	fmt.Println("Conexión exitosa")
	db = connection
}

// Cierra la conexión
func Close() {
	db.Close()
}

// Verificar la conexión
func Ping() {
	if err := db.Ping(); err != nil {
		panic(err)
	}
}

// Crea una tabla
func CreateTable(schema string) {
	db.Exec(schema)
}
