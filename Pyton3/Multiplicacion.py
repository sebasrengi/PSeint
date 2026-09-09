print("Programa para mostrar la tabla de multiplicar de una cantidad de numeros ingresada por el usuario")
n = int(input("¿Qué cantidad de números ingresará?: "))
for i in range(1, n + 1):
    Num = int(input("Ingrese el número " + str(i) + ": "))
    if Num > 0:
          Potencia = 0
          mayores = Num
          print("La potencia de", Num)
          print("Tabla de potencia","\n", mayores**2,"\n",  mayores**3,"\n",  mayores**4,"\n",  mayores**5,"\n",  mayores**6,"\n",  mayores**7,"\n",  mayores**8,"\n",  mayores**9,"\n",  mayores**10 )
    else:
        print("Valor ingresado inválido")