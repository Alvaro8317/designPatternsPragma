from abc import ABC, abstractmethod

class Component(ABC):
    """
    Interfaz Componente que define la operación a realizar.
    """
    @abstractmethod
    def operation(self):
        pass

class ConcreteComponent(Component):
    """
    Clase concreta que implementa la operación a realizar.
    """
    def operation(self):
        return "Operación realizada por ConcreteComponent"

class Decorator(Component):
    """
    Clase abstracta decoradora que define la operación a realizar
    y la instancia de Component a decorar.
    """
    def __init__(self, component: Component):
        self._component = component

    @abstractmethod
    def operation(self):
        pass

class ConcreteDecoratorA(Decorator):
    """
    Clase concreta de Decorator que agrega funcionalidad adicional
    a la operación definida en Component.
    """
    def operation(self):
        return f"Operación realizada por ConcreteDecoratorA({self._component.operation()})"

class ConcreteDecoratorB(Decorator):
    """
    Clase concreta de Decorator que agrega funcionalidad adicional
    a la operación definida en Component.
    """
    def operation(self):
        return f"Operación realizada por ConcreteDecoratorB({self._component.operation()})"

if __name__ == "__main__":
    # Creamos un objeto de ConcreteComponent
    component = ConcreteComponent()

    # Decoramos ConcreteComponent con ConcreteDecoratorA
    decorator_a = ConcreteDecoratorA(component)
    print(decorator_a.operation())

    # Decoramos ConcreteComponent con ConcreteDecoratorB
    decorator_b = ConcreteDecoratorB(component)
    print(decorator_b.operation())

    # Decoramos ConcreteComponent con ConcreteDecoratorA y luego con ConcreteDecoratorB
    decorator_a_b = ConcreteDecoratorB(decorator_a)
    print(decorator_a_b.operation())