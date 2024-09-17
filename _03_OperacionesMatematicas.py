# -------- Operaciones Matemáticas con opción de reiniciar o salir --------

# Definimos el programa dentro de una función para poder reiniciarlo fácilmente
def iniciar_programa():
    # Capítulo 7: Suma, resta, multiplicación y división

    # Solicitamos dos números al usuario
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))

    # Realizamos operaciones básicas
    suma = num1 + num2
    resta = num1 - num2
    multiplicacion = num1 * num2
    division = num1 / num2 if num2 != 0 else "No se puede dividir por cero"

    # Mostramos los resultados de las operaciones
    print("\nOperaciones Básicas:")
    print(f"Suma: {num1} + {num2} = {suma}")
    print(f"Resta: {num1} - {num2} = {resta}")
    print(f"Multiplicación: {num1} * {num2} = {multiplicacion}")
    print(f"División: {num1} / {num2} = {division}")

    # Capítulo 8: Cómo calcular exponentes en Python

    # Solicitamos la base y el exponente
    base = float(input("\nIngresa la base para calcular el exponente: "))
    exponente = float(input("Ingresa el exponente: "))

    # Calculamos el exponente
    resultado_exponente = base ** exponente

    # Mostramos el resultado del cálculo de exponente
    print(f"\n{base} elevado a {exponente} es igual a {resultado_exponente}")

    # Capítulo 9: Los floats y el método round()

    # Solicitamos un número flotante al usuario
    numero_flotante = float(input("\nIngresa un número flotante: "))

    # Redondeamos el número flotante a dos decimales
    numero_redondeado = round(numero_flotante, 2)

    # Mostramos el número original y el redondeado
    print(f"\nNúmero original: {numero_flotante}")
    print(f"Número redondeado a dos decimales: {numero_redondeado}")

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
