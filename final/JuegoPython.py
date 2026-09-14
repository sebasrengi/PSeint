print("==========================================")
print("       JUEGO DE PREGUNTAS")
print("          PROGRAMACIÓN")
print("==========================================")
print()
nombre = input("Ingrese su nombre: ")
print()
print("Hola", nombre)
print("Responde las siguientes preguntas.")
print("Escribe a, b o c.")
print()
puntos = 0
# PREGUNTA 1
print("1. ¿Qué es un algoritmo?")
print("a. Un lenguaje de programación")
print("b. Un conjunto de pasos para resolver un problema")
print("c. Un tipo de computadora")
respuesta = input("Respuesta: ")
if respuesta == "b":
    print("¡Correcto!")
    puntos = puntos + 1
else:
    print("Incorrecto. La respuesta era b.")
print()
print("2. ¿Cuál de los siguientes es un lenguaje de programación?")
print("a. Python")
print("b. Windows")
print("c. Google")
respuesta = input("Respuesta: ")
if respuesta == "a":
    print("¡Correcto!")
    puntos = puntos + 1
else:
    print("Incorrecto. La respuesta era a.")
print()
print("3. ¿Qué paradigma indica principalmente CÓMO realizar una tarea?")
print("a. Declarativo")
print("b. Imperativo")
print("c. Lógico")
respuesta = input("Respuesta: ")
if respuesta == "b":
    print("¡Correcto!")
    puntos = puntos + 1
else:
    print("Incorrecto. La respuesta era b.")
print()
# PREGUNTA 4
print("4. ¿Qué parte de una aplicación se encarga de la interfaz que ve el usuario?")
print("a. Backend")
print("b. Base de datos")
print("c. Frontend")
respuesta = input("Respuesta: ")
if respuesta == "c":
    print("¡Correcto!")
    puntos = puntos + 1
else:
    print("Incorrecto. La respuesta era c.")
print()
print("5. ¿Qué es una variable?")
print("a. Un espacio donde se almacena un dato")
print("b. Un error del programa")
print("c. Una página web")
respuesta = input("Respuesta: ")
if respuesta == "a":
    print("¡Correcto!")
    puntos = puntos + 1
else:
    print("Incorrecto. La respuesta era a.")
print()
print("6. ¿Qué estructura utilizamos para tomar decisiones?")
print("a. if")
print("b. for")
print("c. print")
respuesta = input("Respuesta: ")
if respuesta == "a":
    print("¡Correcto!")
    puntos = puntos + 1
else:
    print("Incorrecto. La respuesta era a.")
print()
# PREGUNTA 7
print("7. ¿Para qué se utiliza principalmente un ciclo for?")
print("a. Para repetir instrucciones")
print("b. Para crear una variable")
print("c. Para cerrar Python")
respuesta = input("Respuesta: ")
if respuesta == "a":
    print("¡Correcto!")
    puntos = puntos + 1
else:
    print("Incorrecto. La respuesta era a.")
print()
print("8. ¿Cuál de estos es un tipo de dato en Python?")
print("a. Real")
print("b. String")
print("c. Pantalla")
respuesta = input("Respuesta: ")
if respuesta == "b":
    print("¡Correcto!")
    puntos = puntos + 1
else:
    print("Incorrecto. La respuesta era b.")
print()
print("9. ¿Cuál es la función de un compilador?")
print("a. Convertir el código para que pueda ser ejecutado")
print("b. Mostrar imágenes")
print("c. Crear páginas web automáticamente")
respuesta = input("Respuesta: ")
if respuesta == "a":
    print("¡Correcto!")
    puntos = puntos + 1
else:
    print("Incorrecto. La respuesta era a.")
print()
# PREGUNTA 10
print("10. ¿Qué función permite mostrar información en pantalla en Python?")
print("a. input()")
print("b. print()")
print("c. for()")
respuesta = input("Respuesta: ")
if respuesta == "b":
    print("¡Correcto!")
    puntos = puntos + 1
else:
    print("Incorrecto. La respuesta era b.")
print("11. ¿Qué hace principalmente un intérprete?")
print("a. Ejecuta el código línea por línea")
print("b. Convierte el código en una imagen")
print("c. Crea automáticamente un computador")
respuesta = input("Respuesta: ")
if respuesta == "a":
    print("¡Correcto!")
    puntos = puntos + 1
else:
    print("Incorrecto. La respuesta era a.")
print()
print("12. ¿Cuál de los siguientes es un operador matemático?")
print("a. +")
print("b. if")
print("c. print")
respuesta = input("Respuesta: ")
if respuesta == "a":
    print("¡Correcto!")
    puntos = puntos + 1
else:
    print("Incorrecto. La respuesta era a.")
print()
# PREGUNTA 13
print("13. ¿Cuál es el orden básico de un programa?")
print("a. Salida → Entrada → Proceso")
print("b. Entrada → Proceso → Salida")
print("c. Proceso → Salida → Entrada")
respuesta = input("Respuesta: ")
if respuesta == "b":
    print("¡Correcto!")
    puntos = puntos + 1
else:
    print("Incorrecto. La respuesta era b.")
print()
print()
print("==========================================")
print("              RESULTADO")
print("==========================================")
print("Jugador:", nombre)
print("Puntos:", puntos, "de 13")
if puntos == 13:
    print("¡Excelente! Dominas muy bien estos temas.")
elif puntos >= 9:
    print("¡Muy bien! Tienes buenos conocimientos.")
elif puntos >= 6:
    print("Bien, pero todavía puedes seguir practicando.")
else:
    print("Necesitas repasar algunos conceptos.")
print()
print("¡Gracias por jugar!")
print("==========================================")