Algoritmo SerieFibonacci
	Escribir"Programa para mostrar una serie de fibonachi "
	Definir mayores, n, Potencia, Num Como Real
	Definir i Como Entero
	mayores <- 0
    Potencia <- 1
    Escribir "Hasta que cantidad desea que llegue la serie " 
	Leer n
	Para i <- 1 Hasta n Hacer
        Escribir ""
        Si n > 0 Entonces
			num <- mayores + Potencia
			Potencia <- mayores
			mayores <- num
			Escribir "Los primeros : ",N " numeros de la serie de fibonachi son : ", Potencia
			Escribir " "
        SiNo
			Escribir "Valor invalido "
        FinSi
	FinPara
FinAlgoritmo