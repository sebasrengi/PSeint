print("Programa para mostrar el promedio de notas de un estudiante")
suma = 0
Potencia = 0
for i in range(1, 5, 1):
    Num = float(input("Ingrese la nota " + str(i) + ": "))
    if Num >= 0:
        Potencia = Num
        suma = suma + Potencia
        if i == 4:
            potencia = suma / 4
            if potencia >= 3.5:
                print("El promedio de notas es de", potencia, "Aprobado")
            else:
                print("El promedio de notas es de", potencia, "Reprobado")
    else:
        print("Valor ingresado inválido")