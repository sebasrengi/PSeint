Algoritmo Descuento1
	Definir cantidad Como Entero
	Definir precio,total, descuento Como Real
	Escribir "Ingrese la cantidad de artículos:"
	Leer cantidad
	Escribir "Ingrese el precio unitario:"
	Leer precio
	total <- cantidad * precio
	Si cantidad > 10 Entonces
		descuento <- total * 0.10
		total <- total - descuento
		Escribir "Se aplicó un descuento del 10%"
		Escribir "El descuento fue de: $ ", descuento " El total a pagar es: $ ", total
	SiNo	
		Escribir "No se aplica descuento, El total a pagar es: $", total
	FinSi
	FinAlgoritmo