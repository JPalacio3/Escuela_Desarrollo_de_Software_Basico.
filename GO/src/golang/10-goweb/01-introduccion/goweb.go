package main

import (
	"fmt"
	"log"
	"net/http"
)

// Handlers: Es una función asociada a un ruta
func Hola(rw http.ResponseWriter, r *http.Request) {
	fmt.Println("El método es: " + r.Method)
	fmt.Fprintln(rw, "Hola mundo desde GO ")
}

func PaginaNF(rw http.ResponseWriter, r *http.Request) {
	http.NotFound(rw, r)
}

func Error(rw http.ResponseWriter, r *http.Request) {
	http.Error(rw, "Este es un error", http.StatusNotFound)
}

func Saludar(rw http.ResponseWriter, r *http.Request) {
	fmt.Println(r.URL)
	fmt.Println(r.URL.RawQuery)
	fmt.Println(r.URL.Query())

	// Obtener un valor mediante su clave en URL
	name := r.URL.Query().Get("name")
	age := r.URL.Query().Get("age")
	fmt.Fprintf(rw, "Hola %s tu edad es %s !!, saludos", name, age)

	// http.Error(rw, "Este es un error", http.StatusNotFound)
}

// Función para imprimir hola mundo

func main() {
	// Mux : Mux es un enrutador (router) de solicitudes HTTP avanzado en Go, proporcionado por el paquete "gorilla/mux", que permite definir rutas y manejar peticiones de manera flexible y modularizada.
	mux := http.NewServeMux()
	mux.HandleFunc("/", Hola)
	mux.HandleFunc("/page", PaginaNF)
	mux.HandleFunc("/error", Error)
	mux.HandleFunc("/saludar", Saludar)

	// Router
	/*
		http.HandleFunc("/", Hola)
		http.HandleFunc("/page", PaginaNF)
		http.HandleFunc("/error", Error)
		http.HandleFunc("/saludar", Saludar)
	*/

	// Creación de servidor
	server := &http.Server{
		Addr:    "localhost:3000",
		Handler: mux,
	}
	fmt.Println("El servidor está corriendo en el puerto 3000")
	fmt.Println("Run Server: http://localhost:3000/")
	// log.Fatal(http.ListenAndServe("localhost:3000", mux))
	log.Fatal(server.ListenAndServe())

}
