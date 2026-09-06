Algoritmo pares
	Escribir"Programa para contar 10 numeros y decir cuales son impares y pares "
	Definir b,c, n Como Entero
	Definir a Como Cadena
	Escribir"escriba su nombre: "
	Leer a
Para i <- 1 Hasta 10 Hacer
		Escribir"ingrese un valor numerico "
		Leer b
		x <- b % 2
	Si x=0 Entonces
			c <- c+1
		SiNo
			n <- n+1
	FinSi
FinPara
Escribir ,a " el total de numeros pares es ",c ", el total de numeros impares es : ",n
FinAlgoritmo