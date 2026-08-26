Algoritmo ClasificarEdad
	Definir edad Como Entero
	Escribir "Ingrese su edad:"
	Leer edad
	Si edad < 12 Entonces
		Escribir "eres un Niño"
	SiNo
		Si edad <= 17 Entonces
			Escribir "eres un Adolescente"
		SiNo
			Escribir "eres un Adulto"
		FinSi
	FinSi
FinAlgoritmo