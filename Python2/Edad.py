print("programa para calcular la edad de alguien")
nom=str(input("escriba su nombre: "))
x=int(input("digite su año de naciminento: "))
y=2026
edad=y-x
if edad<18:
    print("eres menor de edad, tienes ",edad)
else:
    print("eres mayor de edad, tienes ",edad)