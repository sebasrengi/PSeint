Algoritmo DivisibleEntre5o3
	
	Definir numero Como Entero
	
	Escribir "Ingrese un número entero:"
	Leer numero
	
	Si numero MOD 5 = 0 Entonces
		Escribir "El número es divisible entre 5"
	SiNo
		Si numero MOD 3 = 0 Entonces
			Escribir "El número es divisible entre 3"
		SiNo
			Escribir "El número no es múltiplo de 5 ni de 3"
		FinSi
	FinSi
	
FinAlgoritmo