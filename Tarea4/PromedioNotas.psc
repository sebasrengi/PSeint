Algoritmo PromedioNotas
	Escribir "Programa para calcular promedio de notas"
	Definir nota, suma, promedio Como Real
	Definir i Como Entero
	suma <- 0
	Para i <- 1 Hasta 4 Hacer
		Repetir
			Escribir "Ingrese la nota ", i, " (solo numeros entre 0 y 5):"
			Leer nota
			Si nota < 0 O nota > 5 Entonces
				Escribir "Error: solo puede ingresar un numero entre 0 y 5."
			FinSi
		Hasta Que nota >= 0 Y nota <= 5
		suma <- suma + nota
	FinPara
	promedio <- suma / 4
	Escribir "El promedio de las notas es: ", promedio
FinAlgoritmo
