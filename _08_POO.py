# Clase base para una tarea
class Tarea:
    """Clase base para una tarea."""
    
    def __init__(self, descripcion, prioridad):
        """Método inicializador para la clase Tarea.
        - Capítulo 38: El método __init__ - Programación orientada a objetos
        """
        self.descripcion = descripcion
        self.prioridad = prioridad
    
    def mostrar_informacion(self):
        """Muestra la información de la tarea."""
        return f"Descripción: {self.descripcion}, Prioridad: {self.prioridad}"

# Clase derivada para tareas personales
class TareaPersonal(Tarea):
    """Clase derivada para tareas personales."""
    
    def __init__(self, descripcion, prioridad, fecha_vencimiento):
        """Método inicializador para la clase TareaPersonal.
        - Capítulo 42: Cómo heredar propiedades __init__ - Programación orientada a objetos
        """
        super().__init__(descripcion, prioridad)
        self.fecha_vencimiento = fecha_vencimiento
    
    def mostrar_informacion(self):
        """Muestra la información de la tarea personal."""
        # Capítulo 39: ¿Qué es self? - Cambiar valores en objetos - Programación orientada a objetos
        return f"{super().mostrar_informacion()}, Fecha de Vencimiento: {self.fecha_vencimiento}"

# Clase derivada para tareas de trabajo
class TareaTrabajo(Tarea):
    """Clase derivada para tareas de trabajo."""
    
    def __init__(self, descripcion, prioridad, fecha_vencimiento):
        """Método inicializador para la clase TareaTrabajo.
        - Capítulo 42: Cómo heredar propiedades __init__ - Programación orientada a objetos
        """
        super().__init__(descripcion, prioridad)
        self.fecha_vencimiento = fecha_vencimiento
    
    def mostrar_informacion(self):
        """Muestra la información de la tarea de trabajo."""
        # Capítulo 39: ¿Qué es self? - Cambiar valores en objetos - Programación orientada a objetos
        return f"{super().mostrar_informacion()}, Fecha de Vencimiento: {self.fecha_vencimiento}"

# Clase para gestionar las tareas
class GestorTareas:
    """Clase para gestionar una lista de tareas."""
    
    def __init__(self):
        """Método inicializador para la clase GestorTareas.
        - Capítulo 38: El método __init__ - Programación orientada a objetos
        """
        self.tareas = []
    
    def agregar_tarea(self, tarea):
        """Agrega una tarea a la lista."""
        # Capítulo 37: Clases y objetos - Programación orientada a objetos
        self.tareas.append(tarea)
    
    def mostrar_tareas(self):
        """Muestra todas las tareas en la lista."""
        if self.tareas:
            print("\nLista de Tareas:")
            for tarea in self.tareas:
                print(tarea.mostrar_informacion())
                print("-" * 40)
        else:
            print("No hay tareas en la lista.")

def reiniciar_programa():
    """Función lambda para reiniciar el programa."""
    # Capítulo 44: Funciones lambda
    reiniciar = lambda: iniciar_programa()
    reiniciar()

def iniciar_programa():
    gestor = GestorTareas()  # Crear instancia del gestor de tareas
    print("\n--- Gestión de Tareas ---\n")

    while True:
        print("\nOpciones disponibles:")
        print("1. Agregar tarea personal")
        print("2. Agregar tarea de trabajo")
        print("3. Mostrar todas las tareas")
        print("4. Salir o reiniciar")

        opcion = input("\nSelecciona una opción: ")

        if opcion == '1':
            descripcion = input("Introduce la descripción de la tarea: ")
            prioridad = input("Introduce la prioridad de la tarea (alta/media/baja): ")
            fecha_vencimiento = input("Introduce la fecha de vencimiento (dd/mm/aaaa): ")
            tarea = TareaPersonal(descripcion, prioridad, fecha_vencimiento)
            gestor.agregar_tarea(tarea)
            print(f"Tarea personal '{descripcion}' agregada.")

        elif opcion == '2':
            descripcion = input("Introduce la descripción de la tarea: ")
            prioridad = input("Introduce la prioridad de la tarea (alta/media/baja): ")
            fecha_vencimiento = input("Introduce la fecha de vencimiento (dd/mm/aaaa): ")
            tarea = TareaTrabajo(descripcion, prioridad, fecha_vencimiento)
            gestor.agregar_tarea(tarea)
            print(f"Tarea de trabajo '{descripcion}' agregada.")

        elif opcion == '3':
            gestor.mostrar_tareas()

        elif opcion == '4':
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
