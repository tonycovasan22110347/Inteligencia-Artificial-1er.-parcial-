def iniciar_programa():
    print("\n--- Calculadora Interactiva ---\n")

    numeros = []  # Lista para almacenar los números ingresados

    # Capítulo 27: El bucle while
    # Usamos un bucle while para permitir que el usuario ingrese múltiples números
    while True:
        try:
            # Capítulo 23: Input, entrada de datos
            numero = float(input("Introduce un número (o escribe '0' para terminar): "))
            if numero == 0:
                break  # Termina el bucle si se ingresa 0
            numeros.append(numero)  # Se añade el número a la lista
        except ValueError:
            print("Por favor, ingresa un número válido.")
    
    # Verificar si se ingresaron números
    if len(numeros) == 0:
        print("No ingresaste ningún número.")
    else:
        # Capítulo 29: El bucle for
        # Usamos un bucle for para calcular el producto de los números
        suma = sum(numeros)  # Suma de los números
        print(f"\nSuma de los números: {suma}")

        producto = 1
        # Capítulo 30: El bucle for con range()
        for numero in numeros:
            producto *= numero  # Calculamos el producto
        print(f"Producto de los números: {producto}")

        # Capítulo 21: IF y operadores de comparación
        maximo = max(numeros)  # Obtenemos el valor máximo
        minimo = min(numeros)  # Obtenemos el valor mínimo
        print(f"Número máximo: {maximo}")
        print(f"Número mínimo: {minimo}")

        promedio = suma / len(numeros)  # Calculamos el promedio
        print(f"Promedio: {promedio:.2f}")

    # Capítulo 28: El bucle while con condicional if
    # Usamos un bucle while con una condición para permitir al usuario reiniciar o salir
    while True:
        opcion = input("\n¿Deseas reiniciar el programa o salir? (reiniciar/salir): ").lower()
        if opcion == 'reiniciar':  # Si el usuario elige reiniciar
            iniciar_programa()
            break
        elif opcion == 'salir':  # Si elige salir
            print("Programa finalizado. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

# Iniciar el programa
iniciar_programa()
