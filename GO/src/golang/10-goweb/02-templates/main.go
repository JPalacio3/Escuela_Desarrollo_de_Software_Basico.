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
	Activo   bool
	Admin    bool
	Curso    []Curso
}

type Curso struct {
	Nombre string
}

// Funciones
func Saludar() string {
	return "Hola desde una función"
}

// handler
func Index(rw http.ResponseWriter, r *http.Request) {

	funciones := template.FuncMap{
		"saludar": Saludar,
	}

	// c1 := Curso{"GO"}
	// c2 := Curso{"Python"}
	// c3 := Curso{"Java"}
	// c4 := Curso{"Javascript"}

	//fmt.Fprintln(rw, "Hola mundo")
	template, err := template.New("Index.html").Funcs(funciones).ParseFiles("index.html")

	// cursos := []Curso{c1, c2, c3, c4}
	// usuario := Usuario{"Joel", 33, true, true, cursos}

	if err != nil {
		panic(err)
	} else {
		template.Execute(rw, nil)
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
