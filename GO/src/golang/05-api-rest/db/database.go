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

// Verificar si una tabla existe
func ExistTable(tableName string) bool {
	sql := fmt.Sprintf("SHOW TABLES LIKE '%s'", tableName)
	rows, err := db.Query(sql)

	if err != nil {
		println("Error:", err)
	}
	return rows.Next()
}

// Crea una tabla
func CreateTable(schema string, name string) {

	if !ExistTable(name) {
		_, err := db.Exec(schema)
		if err != nil {
			fmt.Println(err)
		}
	}
}

// Polimorfismo de Exec
func Exec(query string, args ...interface{}) (sql.Result, error) {
	Connect()
	result, err := db.Exec(query, args...)
	Close()

	if err != nil {
		fmt.Println(err)
	}
	return result, err
}

// Polimorfizando el Query
func Query(query string, args ...interface{}) (*sql.Rows, error) {
	Connect()
	rows, err := db.Query(query, args...)
	Close()

	if err != nil {
		fmt.Println(err)
	}
	return rows, err
}

// Reiniciar el registro de una tabla con Truncate
func TrancateTable(tableName string) {
	sql := fmt.Sprintf("TRUNCATE %s", tableName)
	Exec(sql)
}
