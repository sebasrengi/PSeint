# ciclo for tabla de multiplicar

num = int(input("Digite un numero del 1 al 9: "))

# Verificar si es par o impar
if num % 2 == 0:
    print("El numero es par")
else:
    print("El numero es impar")

print("Tabla de multiplicar del numero:", num)

for i in range(1, 11):

    result = num * i

    print(num, "X", i, "=", result)