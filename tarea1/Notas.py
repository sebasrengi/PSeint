def calificaciones():
    materias = {
        "Matemáticas": [3.5, 4.0, 4.5, 3.8],
        "Física": [3.0, 3.2, 3.8, 3.5],
        "Programación": [4.5, 4.8, 5.0, 4.6],
        "Química": [2.8, 3.5, 3.0, 3.2],
        "Base de Datos": [4.2, 4.0, 4.3, 4.7],
        "Estadística": [3.6, 3.9, 4.1, 3.8]
    }
    mejor_materia = ""
    mejor_promedio = -1.0
    print("--- Reporte de Calificaciones por Materia ---")
    for materia, notas in materias.items():
        promedio = sum(notas) / len(notas)
        nota_maxima = max(notas) # Nota más alta con max()
        print(f"• Materia: {materia} | Promedio: {promedio:.2f} | Nota Máxima: {nota_maxima}")
        if promedio > mejor_promedio:
            mejor_promedio = promedio
            mejor_materia = materia
    print(f"\n🏆 La materia con mejor promedio es **{mejor_materia}** con un puntaje de {mejor_promedio:.2f}.")
    # Los diccionarios son ideales porque permiten asociar claves únicas (nombres de materias, entre muchos otros usos) 
    # con valores complejos (listas de calificaciones). Esto facilita la búsqueda y el acceso a esa informacion
    # es una forma muy directa de poder acceder a los datos que se quieren
calificaciones()