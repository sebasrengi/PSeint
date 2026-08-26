Algoritmo CalificacionLetra
	Definir nota Como Real
	Escribir "Ingrese la calificación de 0 a 100:"
	Leer nota
	Si nota >= 90 Entonces
		Escribir "Calificación: A"
	SiNo
		Si nota >= 80 Entonces
			Escribir "Calificación: B"
		SiNo
			Si nota >= 70 Entonces
				Escribir "Calificación: C"
			SiNo
				Si nota >= 60 Entonces
					Escribir "Calificación: D"	
				SiNo		
					Escribir "Calificación: F"
				FinSi
			FinSi	
		FinSi	
	FinSi
FinAlgoritmo