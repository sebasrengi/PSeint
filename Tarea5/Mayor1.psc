Algoritmo Mayor1
	Escribir"Programa para contar cuantos numeros son mayores a cero "
	Definir menores, n, mayores, Num Como Real
	Definir i Como Entero
	mayores <- 0
    menores <- 0
    Escribir "Que cantidad de numeros ingresara?: " 
	Leer n
	Para i <- 1 Hasta n Hacer
		Escribir "Ingrese El numero ", i, ": "
        Leer Num
        Si Num > 0 Entonces
			mayores <- mayores + 1
        SiNo
			menores <- menores + 1
        FinSi
	FinPara
	Escribir "El Total de numeros mayores a 0 es : ", mayores " el total de numeros menores a 0 o caracteres diferentes a un numero es : ", menores
FinAlgoritmo