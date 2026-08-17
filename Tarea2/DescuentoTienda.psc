Algoritmo DescuentoTienda
	
	Definir compra, descuento, total Como Real
	
	Escribir "Ingrese el valor de la compra:"
	Leer compra
	
	Si compra >= 100000 Entonces
		descuento <- compra * 0.10
		total <- compra - descuento
	SiNo
		total <- compra
	FinSi
	
	Escribir "El valor a pagar es: $", total
	
FinAlgoritmo