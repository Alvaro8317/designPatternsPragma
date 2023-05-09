from abc import ABC, abstractmethod

# Clase Abstracción
class Forma(ABC):

    def __init__(self, color):
        self.color = color

    @abstractmethod
    def dibujar(self):
        pass


# Clase Implementación
class Color(ABC):

    @abstractmethod
    def colorear(self):
        pass


# Clase Implementación Concreta
class Rojo(Color):

    def colorear(self):
        return "rojo"


# Clase Implementación Concreta
class Azul(Color):

    def colorear(self):
        return "azul"


# Clase Abstracción Refinada
class Cuadrado(Forma):

    def __init__(self, color):
        super().__init__(color)

    def dibujar(self):
        return f"Dibujando un cuadrado de color {self.color.colorear()}"


# Clase Abstracción Refinada
class Circulo(Forma):

    def __init__(self, color):
        super().__init__(color)

    def dibujar(self):
        return f"Dibujando un círculo de color {self.color.colorear()}"


# Ejemplo de uso del patrón Bridge
if __name__ == '__main__':
    # Crear objetos de implementación concreta
    rojo = Rojo()
    azul = Azul()

    # Crear objetos de abstracción refinada, utilizando diferentes implementaciones
    cuadrado_rojo = Cuadrado(rojo)
    cuadrado_azul = Cuadrado(azul)
    circulo_rojo = Circulo(rojo)
    circulo_azul = Circulo(azul)

    # Utilizar los objetos de abstracción refinada para realizar diferentes acciones
    print(cuadrado_rojo.dibujar())
    print(cuadrado_azul.dibujar())
    print(circulo_rojo.dibujar())
    print(circulo_azul.dibujar())
