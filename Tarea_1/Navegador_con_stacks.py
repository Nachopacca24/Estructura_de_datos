



class Navegacion_de_Browser:
    
    def __init__(self):
        self.historial_atras = []
        self.historial_adelante = []
        self.pagina_actual = "Inicio"

    def visitar_pagina(self, nueva_pagina):
        self.historial_atras.append(self.pagina_actual)
        self.pagina_actual = nueva_pagina
        self.historial_adelante.clear()

    def ir_atras(self):
        if self.historial_atras:
            self.historial_adelante.append(self.pagina_actual)
            self.pagina_actual=self.historial_atras.pop()
        else:
            print("No hay páginas atras.")
    
    def ir_adelante(self):
        if self.historial_adelante:
            self.historial_atras.append(self.pagina_actual)
            self.pagina_actual=self.historial_adelante.pop()
        else:
            print("No hay páginas adelante.")


    def mostrar_estado(self):
        print(f"\nPágina actual: {self.pagina_actual}")
        print(f"Historial atrás: {self.historial_atras}")
        print(f"Historial adelante: {self.historial_adelante}")

if __name__ == "__main__":
    navegador = Navegacion_de_Browser()

    while True:
        navegador.mostrar_estado()
        print("Opciones: (1) Visitar nueva página | (2) Atrás | (3) Adelante | (4) Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            nueva_pagina = input("Ingresa la  nueva página: ")
            navegador.visitar_pagina(nueva_pagina)
        elif opcion == "2":
            navegador.ir_atras()
        elif opcion == "3":
            navegador.ir_adelante()
        elif opcion == "4":
            print("Saliendo...")
            break
        else:
            print("Opción no válida.")

