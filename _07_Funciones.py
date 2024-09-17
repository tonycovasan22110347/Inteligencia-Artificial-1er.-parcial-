# Variables globales
contactos = {}

def agregar_contacto(nombre, **detalles):
    """Agrega un nuevo contacto a la agenda."""
    # Capítulo 34: Cómo crear y llamar funciones en Python
    contactos[nombre] = detalles
    return f"Contacto '{nombre}' agregado."

def listar_contactos():
    """Lista todos los contactos en la agenda."""
    # Capítulo 33: Métodos con diccionarios
    if contactos:
        print("\nLista de Contactos:")
        for nombre, detalles in contactos.items():
            detalles_str = ", ".join(f"{k}: {v}" for k, v in detalles.items())
            print(f"Nombre: {nombre}")
            print(f"Detalles: {detalles_str}")
            print("-" * 40)
    else:
        print("No hay contactos en la agenda.")

def buscar_contacto(nombre):
    """Busca un contacto por nombre."""
    # Capítulo 31: ¿Qué son los diccionarios de Python?
    return contactos.get(nombre, "Contacto no encontrado.")

def eliminar_contacto(nombre):
    """Elimina un contacto por nombre."""
    # Capítulo 12: Eliminar elementos con del()
    if nombre in contactos:
        del contactos[nombre]
        return f"Contacto '{nombre}' eliminado."
    return f"Contacto '{nombre}' no encontrado."

def reiniciar_programa():
    """Función lambda para reiniciar el programa."""
    # Capítulo 44: Funciones lambda
    reiniciar = lambda: iniciar_programa()
    reiniciar()

def iniciar_programa():
    print("\n--- Gestión de Contactos ---\n")

    while True:
        print("\nOpciones disponibles:")
        print("1. Agregar contacto")
        print("2. Listar contactos")
        print("3. Buscar contacto")
        print("4. Eliminar contacto")
        print("5. Salir o reiniciar")

        opcion = input("\nSelecciona una opción: ")

        if opcion == '1':
            nombre = input("Introduce el nombre del contacto: ")
            telefono = input("Introduce el teléfono del contacto: ")
            email = input("Introduce el email del contacto (opcional): ")
            detalles = {
                'telefono': telefono,
                'email': email if email else 'No proporcionado'
            }
            resultado = agregar_contacto(nombre, **detalles)
            print(resultado)

        elif opcion == '2':
            listar_contactos()

        elif opcion == '3':
            nombre = input("Introduce el nombre del contacto a buscar: ")
            resultado = buscar_contacto(nombre)
            if resultado != "Contacto no encontrado.":
                print(f"\nContacto encontrado:")
                print(f"Nombre: {nombre}")
                print(f"Detalles: {', '.join(f'{k}: {v}' for k, v in resultado.items())}")
            else:
                print(resultado)

        elif opcion == '4':
            nombre = input("Introduce el nombre del contacto a eliminar: ")
            resultado = eliminar_contacto(nombre)
            print(resultado)

        elif opcion == '5':
            while True:
                decision = input("\n¿Deseas reiniciar el programa o salir? (reiniciar/salir): ").lower()
                if decision == 'reiniciar':
                    reiniciar_programa()  # Reiniciar el programa
                    break
                elif decision == 'salir':
                    print("Programa finalizado. ¡Hasta luego!")
                    return  # Salir del programa
                else:
                    print("Opción no válida. Inténtalo de nuevo.")
        else:
            print("Opción no válida. Por favor, selecciona una opción correcta.")

# Iniciar el programa
iniciar_programa()
