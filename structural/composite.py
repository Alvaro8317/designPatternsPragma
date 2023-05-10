from abc import ABC, abstractmethod

# Clase base para componentes de la estructura jerárquica
class Componente(ABC):

    @abstractmethod
    def operacion(self):
        pass

# Clase hoja de la estructura jerárquica
class Hoja(Componente):

    def __init__(self, nombre):
        self.nombre = nombre

    def operacion(self):
        print(f"Ejecutando operación en la hoja {self.nombre}")

# Clase compuesta de la estructura jerárquica
class Compuesto(Componente):

    def __init__(self, nombre):
        self.nombre = nombre
        self.hojas = []

    def operacion(self):
        print(f"Ejecutando operación en el compuesto {self.nombre}")
        for hoja in self.hojas:
            hoja.operacion()

    def agregar(self, hoja):
        self.hojas.append(hoja)

    def eliminar(self, hoja):
        self.hojas.remove(hoja)


# Ejemplo de uso del patrón Composite
if __name__ == '__main__':
    # Crear una estructura jerárquica compuesta de varias hojas y compuestos
    raiz = Compuesto("Raíz")
    raiz.agregar(Hoja("Hoja 1"))
    raiz.agregar(Hoja("Hoja 2"))

    compuesto1 = Compuesto("Compuesto 1")
    compuesto1.agregar(Hoja("Hoja 3"))
    compuesto1.agregar(Hoja("Hoja 4"))

    compuesto2 = Compuesto("Compuesto 2")
    compuesto2.agregar(Hoja("Hoja 5"))
    compuesto2.agregar(Hoja("Hoja 6"))

    compuesto1.agregar(compuesto2)

    raiz.agregar(compuesto1)

    # Ejecutar una operación en la estructura jerárquica completa
    raiz.operacion()
