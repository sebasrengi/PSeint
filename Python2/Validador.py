print("programa para validar si se puede crear un triangulo ")
a=int(input("digite la longitud del lado 1: "))
b=int(input("digite la longitud del lado 2: "))
c=int(input("digite la longitud del lado 3: "))
if (a + b > c) and (a + c > b) and (b + c > a):
 print("puede formar un triangulo valido")
else:
    print("no puede formar un triangulo")