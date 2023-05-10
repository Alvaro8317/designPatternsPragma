from abc import ABC, abstractmethod

# Clase abstracta para el observador
class Observer(ABC):
    @abstractmethod
    def update(self, pizza):
        pass

# Clase concreta para el observador
class PizzaOrder(Observer):
    def __init__(self, name):
        self.name = name
    
    def update(self, pizza):
        print(f"{self.name}: Pedido de pizza {pizza.flavor} recibido.")

# Clase para el sujeto (pizzería)
class PizzaShop:
    def __init__(self):
        self.observers = []

    def add_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def notify_observers(self, pizza):
        for observer in self.observers:
            observer.update(pizza)

    def place_order(self, pizza):
        self.notify_observers(pizza)

# Clase para el objeto observado (pizza)
class Pizza:
    def __init__(self, flavor):
        self.flavor = flavor

# Ejemplo de uso del patrón Observer
if __name__ == '__main__':
    pizza_shop = PizzaShop()

    # Se agregan dos observadores
    pizza_order_1 = PizzaOrder("Cliente 1")
    pizza_order_2 = PizzaOrder("Cliente 2")

    pizza_shop.add_observer(pizza_order_1)
    pizza_shop.add_observer(pizza_order_2)

    # Se realiza un pedido de pizza
    pizza = Pizza("Pepperoni")
    pizza_shop.place_order(pizza)

    # Se elimina un observador
    pizza_shop.remove_observer(pizza_order_1)

    # Se realiza otro pedido de pizza
    pizza = Pizza("Hawaiana")
    pizza_shop.place_order(pizza)
