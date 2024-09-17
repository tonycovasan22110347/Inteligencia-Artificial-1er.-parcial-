# -------- Manipulación de Cadenas de Texto con opción de reiniciar o salir --------

# Definimos el programa dentro de una función para poder reiniciarlo fácilmente
def iniciar_programa():
    # Capítulo 5: Los métodos upper(), lower() y title()

    # Solicitamos al usuario que ingrese una frase
    frase = input("Escribe una frase: ")

    # Convertimos la frase a mayúsculas usando el método upper()
    frase_mayus = frase.upper()
    print("\nFrase en mayúsculas:")
    print(frase_mayus)

    # Convertimos la frase a minúsculas usando el método lower()
    frase_minus = frase.lower()
    print("\nFrase en minúsculas:")
    print(frase_minus)

    # Convertimos la primera letra de cada palabra a mayúsculas usando title()
    frase_titulo = frase.title()
    print("\nFrase con formato título:")
    print(frase_titulo)

    # Capítulo 6: Saltos de línea y tabulaciones

    # Mostramos un ejemplo de cómo utilizar saltos de línea (\n) y tabulaciones (\t)
    print("\nEjemplo de salto de línea y tabulaciones:")
    print("Primera línea\n\tSegunda línea con tabulación\n\t\tTercera línea con doble tabulación")

    # Combinamos los conceptos anteriores con una frase formateada
    print("\nFrase con formateo adicional:")
    print("\tFrase original:\n\t\t" + frase)
    print("\tFrase en mayúsculas:\n\t\t" + frase_mayus)
    print("\tFrase en minúsculas:\n\t\t" + frase_minus)
    print("\tFrase con formato título:\n\t\t" + frase_titulo)

    # Opción para reiniciar o salir
    while True:
        # Preguntamos si el usuario quiere reiniciar o salir
        reiniciar = input("\n¿Quieres reiniciar el programa o salir? (reiniciar/salir): ").lower()

        if reiniciar == "reiniciar":
            iniciar_programa()  # Llamamos de nuevo a la función para reiniciar el programa
            break  # Salimos del bucle después de reiniciar
        elif reiniciar == "salir":
            print("¡Gracias por usar el programa! Adiós.")
            return  # Termina la función y sale del programa
        else:
            print("Opción no válida. Intenta de nuevo.")  # Mensaje en caso de una entrada inválida

# Iniciamos el programa por primera vez
iniciar_programa()
