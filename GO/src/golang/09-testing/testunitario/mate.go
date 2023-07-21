package testunitario

// Función para probar dos números
func Suma(a, b int) int {
	return a + b
}

// Función para obtener el número mayor
func GetMax(a, b int) int {
	if a > b {
		return a
	} else {
		return b
	}
}

// Función que genera secuencia de fibonacci
func Fibonacci(n int) int {
	if n <= 1 {
		return n
	}
	return Fibonacci(n-1) + Fibonacci(n-2)
}
