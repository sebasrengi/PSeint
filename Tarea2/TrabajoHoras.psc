Algoritmo PagoSemanal
	
	Definir horas, pago Como Real
	
	Escribir "Ingrese las horas trabajadas:"
	Leer horas
	
	Si horas <= 40 Entonces
		pago <- horas * 10000
	SiNo
		pago <- (40 * 10000) + ((horas - 40) * 15000)
	FinSi
	
	Escribir "El pago semanal es: $", pago
	
FinAlgoritmo