# -------- Conceptos Básicos de Python --------

# Definimos el programa dentro de una función para poder reiniciarlo fácilmente
def iniciar_programa():
    # Capítulo 2: Variables y entrada de datos
    # Solicitamos el nombre del usuario
    nombre = input("¿Cuál es tu nombre? ")

    # Capítulo 3: Strings
    # Creamos una variable con un mensaje de saludo usando el nombre ingresado
    saludo = "Hola, " + nombre + "!"

    # Capítulo 4: Cómo concatenar
    # Mostramos el mensaje de saludo concatenando el nombre
    print(saludo)  # Imprime: "Hola, [nombre]!"

    # Capítulo 21: El condicional IF y operadores de comparación
    # Solicitamos la edad del usuario
    edad = int(input("¿Cuántos años tienes? "))

    # Verificamos si la edad es mayor o igual a 18
    if edad >= 18:
        print(nombre + ", eres mayor de edad.")  # Se imprime si la condición es verdadera
    else:
        print(nombre + ", eres menor de edad.")

    # Capítulo 22: El condicional IF ELSE
    # Comprobamos si el usuario es mayor o menor de edad, usando su nombre
    if edad < 18:
        print(nombre + ", eres menor de edad.")
    else:
        print(nombre + ", eres mayor de edad.")

    # Capítulo 23: El condicional IF ELIF ELSE
    # Definimos una comida favorita predefinida
    comida_favorita = input("¿Cuál es tu comida favorita, " + nombre + "? ")

    # Usamos if-elif-else para dar diferentes respuestas según la comida
    if comida_favorita == "pizza":
        print("¡La pizza es deliciosa, " + nombre + "!")
    elif comida_favorita == "hamburguesa":
        print("¡Las hamburguesas son god, " + nombre + "!")
    else:
        print("Tienes gustos exoticos, " + nombre + ".")

    # Capítulo 24: Comprobar datos en listas
    # Ahora permitimos que el usuario agregue frutas a la lista
    frutas = []  # Empezamos con una lista vacía
    agregar_frutas = True

    print("Vamos a crear una lista de frutas, " + nombre + ".")
    
    # Bucle para agregar frutas a la lista
    while agregar_frutas:
        fruta = input("Agrega una fruta a la lista (o escribe 'salir' para finalizar): ")
        if fruta.lower() == "salir":
            agregar_frutas = False
        else:
            frutas.append(fruta)
            print(fruta + " ha sido agregada a la lista.")

    print("Tu lista de frutas es: " + str(frutas))

    # Verificamos si una fruta específica está en la lista
    fruta_a_buscar = input("¿Qué fruta quieres buscar en la lista?: ")
    if fruta_a_buscar in frutas:
        print("¡La " + fruta_a_buscar + " está en la lista de frutas!")
    else:
        print("La " + fruta_a_buscar + " no está en la lista de frutas.")

    # Capítulo 25: Múltiples condiciones IF
    # Verificamos varias condiciones usando 'and'
    if edad >= 18 and "naranja" in frutas:
        print(nombre + ", eres mayor de edad y te gustan las naranjas.")

    # Capítulo 26: Tips para condicionales
    # Verificamos si la lista de frutas tiene elementos
    if frutas:  # Esto comprueba si la lista no está vacía
        print(nombre + ", la lista de frutas no está vacía.")
    else:
        print(nombre + ", la lista de frutas está vacía.")
    
    # Capítulo adicional: Opción para reiniciar o salir
    while True:
        # Preguntamos si el usuario quiere reiniciar o salir
        reiniciar = input("¿Quieres reiniciar el programa o salir? (reiniciar/salir): ").lower()

        if reiniciar == "reiniciar":
            iniciar_programa()  # Llamamos de nuevo a la función para reiniciar el programa
            break  # Salimos del bucle después de reiniciar
        elif reiniciar == "salir":
            print("Adiós, " + nombre + "!")
            return  # Termina la función y sale del programa
        else:
            print("Opción no válida. Intenta de nuevo.")

# Iniciamos el programa por primera vez
iniciar_programa()
