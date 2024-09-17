import json

# Ruta del archivo donde se guardarán los datos
ARCHIVO_DATOS = 'calificaciones.json'

def cargar_datos():
    """Carga los datos del archivo, si existe, y los retorna como un diccionario."""
    try:
        with open(ARCHIVO_DATOS, 'r') as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return {}  # Retorna un diccionario vacío si el archivo no existe

def guardar_datos(calificaciones):
    """Guarda los datos en el archivo."""
    with open(ARCHIVO_DATOS, 'w') as archivo:
        json.dump(calificaciones, archivo, indent=4)

def iniciar_programa():
    print("\n--- Gestión de Calificaciones de Estudiantes ---\n")

    # Cargar los datos del archivo
    calificaciones = cargar_datos()

    # Menú de opciones
    while True:
        print("\nOpciones disponibles:")
        print("1. Agregar calificaciones para un nuevo estudiante")
        print("2. Actualizar calificaciones de un estudiante")
        print("3. Eliminar un estudiante")
        print("4. Ver calificaciones de todos los estudiantes")
        print("5. Ver promedio de un estudiante")
        print("6. Salir o reiniciar")

        opcion = input("\nSelecciona una opción: ")

        # Opción 1: Agregar un nuevo estudiante y sus calificaciones
        if opcion == '1':
            nombre = input("Introduce el nombre del nuevo estudiante: ")
            if nombre in calificaciones:
                print(f"{nombre} ya está en el registro.")
            else:
                try:
                    notas = list(map(int, input(f"Introduce las calificaciones de {nombre} separadas por comas: ").split(',')))
                    calificaciones[nombre] = notas
                    print(f"Calificaciones añadidas para {nombre}.")
                except ValueError:
                    print("Por favor, introduce calificaciones válidas separadas por comas.")
                # Guardar los datos actualizados
                guardar_datos(calificaciones)

        # Opción 2: Actualizar las calificaciones de un estudiante
        elif opcion == '2':
            nombre = input("Introduce el nombre del estudiante a actualizar: ")
            if nombre in calificaciones:
                try:
                    nuevas_notas = list(map(int, input(f"Introduce las nuevas calificaciones de {nombre} separadas por comas: ").split(',')))
                    calificaciones[nombre] = nuevas_notas
                    print(f"Calificaciones actualizadas para {nombre}.")
                except ValueError:
                    print("Por favor, introduce calificaciones válidas separadas por comas.")
                # Guardar los datos actualizados
                guardar_datos(calificaciones)
            else:
                print(f"{nombre} no está en la lista de estudiantes.")

        # Opción 3: Eliminar un estudiante
        elif opcion == '3':
            nombre = input("Introduce el nombre del estudiante a eliminar: ")
            if nombre in calificaciones:
                calificaciones.pop(nombre)  # Usamos el método pop para eliminar
                print(f"{nombre} ha sido eliminado del registro.")
                # Guardar los datos actualizados
                guardar_datos(calificaciones)
            else:
                print(f"{nombre} no está en la lista de estudiantes.")

        # Opción 4: Mostrar todas las calificaciones
        elif opcion == '4':
            if calificaciones:
                print("\nCalificaciones de los estudiantes:")
                for estudiante, notas in calificaciones.items():
                    print(f"{estudiante}: {notas}")
            else:
                print("No hay calificaciones registradas.")

        # Opción 5: Ver el promedio de un estudiante
        elif opcion == '5':
            nombre = input("Introduce el nombre del estudiante para ver su promedio: ")
            if nombre in calificaciones:
                promedio = sum(calificaciones[nombre]) / len(calificaciones[nombre])
                print(f"El promedio de {nombre} es {round(promedio, 2)}.")
            else:
                print(f"{nombre} no está en la lista de estudiantes.")

        # Opción 6: Salir o reiniciar el programa
        elif opcion == '6':
            while True:
                decision = input("\n¿Deseas reiniciar el programa o salir? (reiniciar/salir): ").lower()
                if decision == 'reiniciar':
                    iniciar_programa()  # Reiniciar el programa
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
