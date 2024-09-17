import datetime  # Importa el módulo datetime para trabajar con fechas

# Función para mostrar la fecha y hora actual
def mostrar_fecha_hora_actual():
    """Muestra la fecha y hora actual."""
    # Capítulo 45: Trabajar con fechas con el módulo datetime
    ahora = datetime.datetime.now()  # Obtiene la fecha y hora actual
    print(f"Fecha y Hora Actual: {ahora.strftime('%d/%m/%Y %H:%M:%S')}")  # Muestra la fecha y hora en formato dd/mm/aaaa hh:mm:ss

# Función para calcular la diferencia en días entre dos fechas
def calcular_diferencia_fechas(fecha1, fecha2):
    """Calcula la diferencia en días entre dos fechas.
    - Capítulo 45: Trabajar con fechas con el módulo datetime
    """
    # Convierte las fechas de string a objetos datetime
    fecha1 = datetime.datetime.strptime(fecha1, '%d/%m/%Y')  # Convierte la primera fecha
    fecha2 = datetime.datetime.strptime(fecha2, '%d/%m/%Y')  # Convierte la segunda fecha
    diferencia = fecha2 - fecha1  # Calcula la diferencia entre las dos fechas
    return diferencia.days  # Devuelve la diferencia en días

def reiniciar_programa():
    """Función lambda para reiniciar el programa."""
    # Capítulo 44: Funciones lambda
    reiniciar = lambda: iniciar_programa()
    reiniciar()

def iniciar_programa():
    while True:
        print("\nOpciones disponibles:")
        print("1. Mostrar fecha y hora actual")
        print("2. Calcular diferencia en días entre dos fechas")
        print("3. Salir o reiniciar")

        opcion = input("\nSelecciona una opción: ")

        if opcion == '1':
            mostrar_fecha_hora_actual()  # Muestra la fecha y hora actual

        elif opcion == '2':
            fecha1 = input("Introduce la primera fecha (dd/mm/aaaa): ")
            fecha2 = input("Introduce la segunda fecha (dd/mm/aaaa): ")
            try:
                diferencia_dias = calcular_diferencia_fechas(fecha1, fecha2)  # Calcula la diferencia en días entre las fechas
                print(f"La diferencia entre las fechas es de {diferencia_dias} días.")
            except ValueError:
                print("Formato de fecha inválido. Asegúrate de usar el formato dd/mm/aaaa.")

        elif opcion == '3':
            while True:
                decision = input("\n¿Deseas reiniciar el programa o salir? (reiniciar/salir): ").lower()
                if decision == 'reiniciar':
                    reiniciar_programa()  # Reinicia el programa
                    break
                elif decision == 'salir':
                    print("Programa finalizado. ¡Hasta luego!")
                    return  # Sale del programa
                else:
                    print("Opción no válida. Inténtalo de nuevo.")
        else:
            print("Opción no válida. Por favor, selecciona una opción correcta.")

# Iniciar el programa
iniciar_programa()
