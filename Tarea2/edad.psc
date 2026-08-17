Algoritmo CINE
	
	Definir edad, precio Como Entero
	
	Escribir "Ingrese la edad del usuario:"
	Leer edad
	
	Si edad <= 12 Entonces
		precio <- 8000
		Escribir "El precio de la entrada es: $", precio
		
	SiNo
		Si edad <= 60 Entonces
			precio <- 15000
			Escribir "El precio de la entrada es: $", precio
			
		SiNo
			precio <- 10000
			Escribir "El precio de la entrada es: $", precio
		FinSi
	FinSi
	
FinAlgoritmo