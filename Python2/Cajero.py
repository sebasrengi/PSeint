print("programa que emula un cajero automatico")
nom=str(input("escriba su nombre de usuario: "))
x=int(input("digite su Clave: "))
saldo=200000
if nom == "admin" and x == 1234:
    print("Acceso concedido ")
    while True:
        print("1. Consultar saldo")
        print("2. Retirar dinero")
        print("3. Depositar dinero")
        print("4. Salir")
        operacion=int(input("Que operacion desea realizar: "))
        if operacion == 1:
            print("Su saldo actual es: $", saldo)
        elif operacion == 2:
            retiro = float(input("Ingrese el valor a retirar: $"))
            if retiro <= 0:
                print("El valor debe ser mayor a cero.")
            elif retiro > saldo:
                print("Fondos insuficientes.")
            else:
                saldo = saldo - retiro
                print("Retiro realizado correctamente.")
                print("Su nuevo saldo es: $", saldo)
        elif operacion == 3:
            deposito = float(input("Ingrese el valor a depositar: $"))
            if deposito <= 0:
                print("El valor debe ser mayor a cero.")
                saldo = saldo + deposito
                print("Depósito realizado correctamente.")
                print("Su nuevo saldo es: $", saldo)
        elif operacion == 4:
            print("Gracias por utilizar el cajero automático.")
        else:
            print("Opcion invalida")
        break
else:
    print("Datos incorrectos, acceso denegado ")