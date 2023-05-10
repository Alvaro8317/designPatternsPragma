import random

# Clase Flyweight
class Flyweight:
    """
    La clase Flyweight define el estado intrínseco del objeto compartido.
    Los objetos Flyweight almacenan información que se comparte entre varias
    instancias de la clase. Esta información no cambia entre las instancias
    del objeto, y se puede compartir en lugar de crear nuevos objetos para cada instancia.
    """

    def __init__(self, shared_state):
        self.shared_state = shared_state

    def operation(self, unique_state):
        """
        La operación que realiza el Flyweight utiliza tanto el estado
        intrínseco compartido como el estado único de la instancia actual.
        """
        s = f"Flyweight: Shared('{self.shared_state}') and Unique('{unique_state}')"
        return s

# Clase FlyweightFactory
class FlyweightFactory:
    """
    La clase FlyweightFactory administra los objetos Flyweight y garantiza
    que se compartan correctamente entre las instancias de la clase.
    """

    def __init__(self):
        self.flyweights = {}

    def get_flyweight(self, shared_state):
        """
        Devuelve un objeto Flyweight existente con el estado compartido especificado,
        o crea uno nuevo si aún no existe.
        """
        if shared_state not in self.flyweights:
            self.flyweights[shared_state] = Flyweight(shared_state)
        return self.flyweights[shared_state]

    def list_flyweights(self):
        """
        Devuelve una cadena con información sobre la cantidad de objetos Flyweight
        existentes en el Factory.
        """
        return f"FlyweightFactory: {len(self.flyweights)} flyweights."

# Función auxiliar
def random_shared_state():
    """
    Devuelve un estado compartido aleatorio entre un conjunto predefinido de estados.
    """
    return random.choice(["state A", "state B", "state C"])

if __name__ == "__main__":
    # Creamos una instancia de FlyweightFactory
    factory = FlyweightFactory()

    # Creamos 10 instancias de Flyweight con estados compartidos aleatorios
    for i in range(10):
        flyweight = factory.get_flyweight(random_shared_state())
        print(f"Flyweight: {flyweight.operation('unique state')}")

    # Imprimimos el número total de objetos Flyweight creados
    print(factory.list_flyweights())
