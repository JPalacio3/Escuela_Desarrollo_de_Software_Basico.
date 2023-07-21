package testunitario

import "testing"

/*
func TestSuma(t *testing.T) {

	total := Suma(5, 5)

	if total != 10 {
		t.Errorf("Suma incorrecta, tiene %d, se esperaba %d", total, 10)
	}
}

/*
SALIDA:
PASS
ok      github.com/JPalacio3/Escuela_Desarrollo_de_Software_Basico.2Parte/tree/master/GO/09-testing    0.346s
*/

// test tradicional
func TestSuma(t *testing.T) {
	tabla := []struct {
		a int
		b int
		c int
	}{
		{1, 2, 3},
		{2, 2, 4},
		{25, 25, 50},
	}

	for _, item := range tabla {
		total := Suma(item.a, item.b)

		if total != item.c {
			t.Errorf("Suma incorrecta, tiene %d, se esperaba %d", item.c, total)
		}
	}
}

/*
SALIDA:
λ go test
--- FAIL: TestSuma (0.00s)
    mate_test.go:37: Suma incorrecta, tiene 51, se esperaba 50
FAIL
exit status 1
FAIL    github.com/JPalacio3/Escuela_Desarrollo_de_Software_Basico.2Parte/tree/
master/GO/09-testing    0.365s
*/

func TestGetMax(t *testing.T) {
	tabla := []struct {
		a int
		b int
		c int
	}{
		{4, 2, 4},
		{2, 6, 6},
		{2, 3, 3},
	}

	for _, item := range tabla {
		max := GetMax(item.a, item.b)

		if max != item.c {
			t.Errorf("GetMax incorrecta, tiene %d, se esperaba %d", max, item.c)
		}
	}
}

func TestFibo(t *testing.T) {
	tabla := []struct {
		n int
		r int
	}{
		{1, 1},
		{8, 21},
		{50, 12586269025},
	}

	for _, item := range tabla {
		fibo := Fibonacci(item.n)

		if fibo != item.r {
			t.Errorf("GetMax incorrecta, tiene %d, se esperaba %d", fibo, item.r)
		}
	}
}
