Algoritmo Potencia2
	Escribir"Programa para mostrar tabla de potencia de un numero hasta la decima potencia "
	Definir menores, Potencia, Num Como Real
	Definir i Como Entero
    Escribir "Cual es tu nombre: " 
	Leer n
	Para i <- 1 Hasta 5 Hacer
		Escribir "Ingrese El numero ", i, ": "
        Leer Num
        Si Num > 0 Entonces
			Potencia <- 0
			mayores <- Potencia + Num
			mayores <- mayores * mayores * mayores * mayores * mayores * mayores * mayores * mayores * mayores * mayores 
			Escribir n, " La potencia de : ",Num " es: ", mayores
			Escribir " "
        SiNo
			Escribir "Valor ingresado invalido "
        FinSi
	FinPara
FinAlgoritmo