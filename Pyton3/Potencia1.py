print("Programa para mostrar la potencia de un número hasta la décima potencia")
n = int(input("¿Qué cantidad de números ingresará?: "))
for i in range(1, n + 1):
    Num = int(input("Ingrese el número " + str(i) + ": "))
    if Num > 0:
        Potencia = Num ** 10
        print("La potencia de", Num, " hasta la décima potencia es:", Num**2,"\n",  Num**3,"\n",  Num**4,"\n",  Num**5,"\n",  Num**6,"\n",  Num**7,"\n",  Num**8,"\n",  Num**9,"\n",  Num**10 )
    else:
        print("Valor ingresado inválido")