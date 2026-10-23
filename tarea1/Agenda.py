def gestionar_agenda():
    agenda = {
        "Ana Gómez": "3101234567",
        "Carlos Ruiz": "3209876543",
        "Lucía Pérez": "3154567890",
        "Mateo Silva": "3112223344",
        "Sofía Torres": "3185556677",
        "David Morales": "3167778899",
        "Valeria Ríos": "3123334455",
        "Andrés Castro": "3194445566",
        "Camila Rojas": "3138889900",
        "Jorge Blanco": "3146667788"
    }

    while True:
        print("--- CONSULTAR CONTACTO ---")
        consulta = input("Consulte los contactos que quiera en caso contrario escriba 'No registrado': ")
        resultado = agenda.get(consulta, "No registrado")
        print(f"Resultado de búsqueda para '{consulta}': {resultado}\n")

        if consulta == "No registrado":
            break
        print("consulta exitosa")
    print("--- AGREGAR NUEVO CONTACTO ---")
    nuevo_nombre = input("Ingrese el nombre del nuevo contacto: ")
    nuevo_tel = input(f"Ingrese el teléfono de {nuevo_nombre}: ")
    agenda[nuevo_nombre] = nuevo_tel
    print(f"¡Contacto '{nuevo_nombre}' agregado exitosamente!\n")
    print("--- MODIFICAR / SOBREESCRIBIR TELÉFONO ---")
    mod_nombre = input("Ingrese el nombre del contacto cuyo teléfono desea actualizar: ")
    if mod_nombre in agenda:
        nuevo_tel_mod = input(f"Ingrese el nuevo teléfono para {mod_nombre}: ")
        agenda[mod_nombre] = nuevo_tel_mod
        print(f"Teléfono de '{mod_nombre}' actualizado correctamente.\n")
    else:
        print("El contacto no existe en la agenda.\n")

    print("--- ELIMINAR UN CONTACTO ---")
    elim_nombre = input("Ingrese el nombre del contacto que desea eliminar: ")
    if elim_nombre in agenda:
        del agenda[elim_nombre]
        print(f"Contacto '{elim_nombre}' eliminado con éxito.\n")
    else:
        print("El contacto no se encontraba en la agenda.\n")

    print("--- AGENDA FINAL COMPLETA ---")
    for nombre, telefono in agenda.items():
        print(f"• {nombre}: {telefono}")

gestionar_agenda()