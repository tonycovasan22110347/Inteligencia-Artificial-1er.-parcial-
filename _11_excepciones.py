def suma(a, b):
    """
    Función para sumar dos números.
    Utiliza manejo de excepciones para asegurar que los valores sean numéricos.
    - Capítulo 51: Manejo de excepciones
    """
    try:
        return a + b
    except TypeError:
        return "Error: Ambos valores deben ser numéricos."

def resta(a, b):
    """
    Función para restar dos números.
    Utiliza manejo de excepciones para asegurar que los valores sean numéricos.
    - Capítulo 51: Manejo de excepciones
    """
    try:
        return a - b
    except TypeError:
        return "Error: Ambos valores deben ser numéricos."

def multiplicacion(a, b):
    """
    Función para multiplicar dos números.
    Utiliza manejo de excepciones para asegurar que los valores sean numéricos.
    - Capítulo 51: Manejo de excepciones
    """
    try:
        return a * b
    except TypeError:
        return "Error: Ambos valores deben ser numéricos."

def division(a, b):
    """
    Función para dividir dos números.
    Utiliza manejo de excepciones para manejar la división por cero y asegurarse de que los valores sean numéricos.
    - Capítulo 51: Manejo de excepciones
    """
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: No se puede dividir por cero."
    except TypeError:
        return "Error: Ambos valores deben ser numéricos."

def leer_numero(mensaje):
    """
    Función para leer un número del usuario.
    Utiliza manejo de excepciones para manejar entradas no válidas.
    - Capítulo 51: Manejo de excepciones
    """
    while True:
        try:
            numero = float(input(mensaje))
            return numero
        except ValueError:
            print("Error: Por favor, introduce un número válido.")

def iniciar_calculadora():
    """
    Función principal para iniciar la calculadora.
    Permite al usuario realizar operaciones matemáticas básicas y manejar excepciones.
    - Capítulo 51: Manejo de excepciones
    """
    while True:
        print("\nOpciones disponibles:")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Salir")

        opcion = input("\nSelecciona una opción: ")

        if opcion in ['1', '2', '3', '4']:
            print("Introduce dos números para la operación.")
            num1 = leer_numero("Introduce el primer número: ")
            num2 = leer_numero("Introduce el segundo número: ")

            if opcion == '1':
                print(f"Resultado: {suma(num1, num2)}")
            elif opcion == '2':
                print(f"Resultado: {resta(num1, num2)}")
            elif opcion == '3':
                print(f"Resultado: {multiplicacion(num1, num2)}")
            elif opcion == '4':
                print(f"Resultado: {division(num1, num2)}")
        elif opcion == '5':
            print("Programa finalizado. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, selecciona una opción correcta.")

# Iniciar la calculadora
iniciar_calculadora()
