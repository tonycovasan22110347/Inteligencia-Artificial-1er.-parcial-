import re  # Importa el módulo re para trabajar con expresiones regulares

def buscar_email(texto):
    """Busca un correo electrónico en el texto utilizando search().
    - Capítulo 47: Expresiones regulares - search()
    """
    patron_email = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'  # Patrón para buscar correos electrónicos
    resultado = re.search(patron_email, texto)
    if resultado:
        return f"Correo electrónico encontrado: {resultado.group()}"
    else:
        return "No se encontró ningún correo electrónico."

def encontrar_digitos(texto):
    """Encuentra todos los dígitos en el texto utilizando findall().
    - Capítulo 48: Expresiones regulares - findall()
    """
    patron_digitos = r'\d+'  # Patrón para encontrar dígitos
    resultados = re.findall(patron_digitos, texto)
    if resultados:
        return f"Dígitos encontrados: {', '.join(resultados)}"
    else:
        return "No se encontraron dígitos."

def dividir_texto_por_punto_y_coma(texto):
    """Divide el texto en partes utilizando split().
    - Capítulo 49: Expresiones regulares - split()
    """
    partes = re.split(r'[;]', texto)  # Divide el texto por punto y coma
    return f"Partes del texto: {', '.join(partes)}"

def limpiar_texto(texto):
    """Reemplaza múltiples espacios con un solo espacio utilizando sub().
    - Capítulo 49: Expresiones regulares - sub()
    """
    texto_limpio = re.sub(r'\s+', ' ', texto)  # Reemplaza uno o más espacios con un solo espacio
    return f"Texto después de limpiar espacios: {texto_limpio}"

def patrones_especiales():
    """Muestra ejemplos de secuencias especiales y metacaracteres en RegEx.
    - Capítulo 50: Secuencias especiales, metacaracteres y sets - Expresiones regulares – RegEx
    """
    texto = "Fecha: 2024-09-17, Teléfono: 123-456-7890, Código Postal: 12345"
    patrones = {
        'Fecha (YYYY-MM-DD)': r'\d{4}-\d{2}-\d{2}',  # Secuencia para fecha en formato YYYY-MM-DD
        'Número de Teléfono': r'\d{3}-\d{3}-\d{4}',  # Secuencia para número de teléfono en formato 123-456-7890
        'Código Postal': r'\d{5}'  # Secuencia para código postal de 5 dígitos
    }
    resultados = {desc: re.findall(patron, texto) for desc, patron in patrones.items()}
    return '\n'.join([f"{desc}: {', '.join(res)}" for desc, res in resultados.items()])

def reiniciar_programa():
    """Función lambda para reiniciar el programa."""
    reiniciar = lambda: iniciar_programa()
    reiniciar()

def iniciar_programa():
    while True:
        print("\nOpciones disponibles:")
        print("1. Buscar correo electrónico")
        print("2. Encontrar dígitos en texto")
        print("3. Dividir texto por punto y coma")
        print("4. Limpiar texto de múltiples espacios")
        print("5. Mostrar patrones especiales y metacaracteres")
        print("6. Salir o reiniciar")

        opcion = input("\nSelecciona una opción: ")

        if opcion == '1':
            texto = input("Introduce el texto para buscar un correo electrónico: ")
            print(buscar_email(texto))

        elif opcion == '2':
            texto = input("Introduce el texto para encontrar dígitos: ")
            print(encontrar_digitos(texto))

        elif opcion == '3':
            texto = input("Introduce el texto para dividir por punto y coma: ")
            print(dividir_texto_por_punto_y_coma(texto))

        elif opcion == '4':
            texto = input("Introduce el texto para limpiar de múltiples espacios: ")
            print(limpiar_texto(texto))

        elif opcion == '5':
            print(patrones_especiales())

        elif opcion == '6':
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
