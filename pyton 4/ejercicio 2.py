cantidad = int(input("¿Cuántos triángulos desea calcular?: "))

for i in range(cantidad):
    print(f"\n--- Triángulo {i+1} ---")
    x = float(input("Digita la base del triangulo: "))
    y = float(input("Digita la altura del triangulo: "))
    
    if x > 0 and y > 0:
        area = (x * y) / 2
        print("El area del triangulo es:", area)
    else:
        print("Error: La base y la altura deben ser valores positivos.")