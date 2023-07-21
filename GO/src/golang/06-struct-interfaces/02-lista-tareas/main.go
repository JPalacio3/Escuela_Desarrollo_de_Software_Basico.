package main

import "fmt"

// Tareas
type Task struct {
	name     string
	desc     string
	complete bool
}

// Métodos para las tareas
func (t *Task) toPrint() {
	fmt.Printf("Nombre: %s\nDescripción: %s\nCompletado: %t\n", t.name, t.desc, t.complete)
}

func (t *Task) markComplete() {
	t.complete = true
}

// Lista de tareas
type TaskList struct {
	tasks []*Task
}

// Métodos para las listas de tareas
func (tl *TaskList) appendTask(t *Task) {
	tl.tasks = append(tl.tasks, t)
}

func (tl *TaskList) deleteTask(index int) {
	tl.tasks = append(tl.tasks[:index], tl.tasks[index+1:]...)
}

func main() {

	t1 := Task{
		name:     "Curso de GO",
		desc:     "Completar curso de GO hoy mismo",
		complete: true,
	}
	t2 := Task{
		name:     "Curso de Javascript",
		desc:     "Comenzar con el curso de Javascript profundo este mes",
		complete: false,
	}

	t3 := Task{
		name:     "Curso de Python",
		desc:     "Profundizar Python a nivel avanzado en el transcurso de este año",
		complete: false,
	}

	lista := TaskList{}
	lista.appendTask(&t1)
	lista.appendTask(&t2)
	lista.appendTask(&t3)

	fmt.Println(lista)

	lista.deleteTask(1)

	for i, task := range lista.tasks {
		fmt.Println(i, task.name)
	}

	/*
		fmt.Println()
		t1.toPrint()

		fmt.Println()
		t2.toPrint()
	*/
}

/*
Se muestra una implementación simple de una lista de tareas (TaskList) utilizando estructuras y métodos.

En primer lugar, se define la estructura Task para representar una tarea, que contiene los campos name (nombre de la tarea), desc (descripción de la tarea) y complete (indicador de si la tarea está completa o no).

A continuación, se definen los métodos asociados a las tareas. El método toPrint() imprime los detalles de una tarea en la consola. El método markComplete() establece la propiedad complete de una tarea como verdadera.

Luego, se define la estructura TaskList para representar una lista de tareas, que contiene un slice de punteros a objetos Task.

Se implementan métodos asociados a las listas de tareas. El método appendTask() agrega una tarea al final de la lista. El método deleteTask() elimina una tarea de la lista dado su índice.

En la función main(), se crean tres tareas (t1, t2, t3) y se agregan a la lista utilizando el método appendTask(). Luego, se imprime la lista de tareas completa utilizando fmt.Println().

A continuación, se llama al método deleteTask() para eliminar la segunda tarea de la lista.

Finalmente, se itera sobre la lista de tareas restante utilizando un bucle for y se imprime el índice y el nombre de cada tarea en la lista.

*/
