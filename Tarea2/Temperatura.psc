Algoritmo TemperaturaClima
	
	Definir temperatura Como Real
	
	Escribir "Ingrese la temperatura en grados Celsius:"
	Leer temperatura
	
	Si temperatura < 15 Entonces
		Escribir "El clima está Frío"
	SiNo
		Si temperatura <= 28 Entonces
			Escribir "El clima está Templado"
		SiNo
			Escribir "El clima está Caluroso"
		FinSi
	FinSi
	
FinAlgoritmo