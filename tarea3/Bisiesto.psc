Algoritmo Bisiesto
	Definir año Como Entero
	Escribir "Ingrese un año:"
	Leer año
	Si (año MOD 4 = 0 Y ano MOD 100 <> 0) O (ano MOD 400 = 0) Entonces
		Escribir "El año ", año, " es bisiesto"
	SiNo
		Escribir "El año ", año, " no es bisiesto"
	FinSi
FinAlgoritmo