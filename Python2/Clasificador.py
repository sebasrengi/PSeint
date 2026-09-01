print("programa para validar y clasificar tipos de triangulos ")
a=int(input("digite la longitud del lado 1: "))
b=int(input("digite la longitud del lado 2: "))
c=int(input("digite la longitud del lado 3: "))
if (a + b > c) and (a + c > b) and (b + c > a):
 print("puede formar un triangulo valido")
    if a == b == c :
        print("es un equilatero")
    elif a == b or a == c or b == c :
     print("es un isosceles")
    else:
        print("es un escaleno") 
else:
    print("no puede formar un triangulo")