package main

import (
	"fmt"
	"html/template"
	"log"
	"net/http"
)

// Estructura
type Usuario struct {
	UserName string
	Edad     int
}

// handler
func Index(rw http.ResponseWriter, r *http.Request) {
	//fmt.Fprintln(rw, "Hola mundo")
	template, err := template.ParseFiles("index.html")

	usuario := Usuario{"Joel", 33}
	if err != nil {
		panic(err)
	} else {
		template.Execute(rw, usuario)
	}

}

func main() {
	// mux
	mux := http.NewServeMux()
	mux.HandleFunc("/", Index)

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
