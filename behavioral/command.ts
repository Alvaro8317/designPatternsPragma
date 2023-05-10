// Interfaz Command que define el método para ejecutar y deshacer un comando
interface Command {
  execute(): void;
  undo(): void;
}

// Clase PizzaOrder que implementa Command y representa un pedido de pizza
class PizzaOrder implements Command {
  private type: string;
  private toppings: string[];
  private price: number;

  constructor(type: string, toppings: string[], price: number) {
    this.type = type;
    this.toppings = toppings;
    this.price = price;
  }

  execute(): void {
    console.log(
      `Preparando pizza ${this.type} con ${this.toppings.join(
        ', '
      )} - Precio: ${this.price}$`
    );
  }

  undo(): void {
    console.log(
      `Deshaciendo pizza ${this.type} con ${this.toppings.join(
        ', '
      )} - Precio: ${this.price}$`
    );
  }
}

// Clase PizzaOrderManager que maneja los pedidos de pizza
class PizzaOrderManager {
  private orders: Command[] = [];

  addOrder(order: Command): void {
    this.orders.push(order);
    order.execute();
  }

  undoLastOrder(): void {
    const lastOrder = this.orders.pop();
    if (lastOrder) {
      lastOrder.undo();
    } else {
      console.log('No hay pedidos para deshacer');
    }
  }
}

// Ejemplo de uso
const pizzaOrderManager = new PizzaOrderManager();

const order1 = new PizzaOrder('Margarita', ['queso'], 10);
const order2 = new PizzaOrder('Hawaiana', ['piña', 'jamón'], 12);
const order3 = new PizzaOrder('Pepperoni', ['pepperoni'], 14);

pizzaOrderManager.addOrder(order1);
pizzaOrderManager.addOrder(order2);
pizzaOrderManager.addOrder(order3);

pizzaOrderManager.undoLastOrder();
pizzaOrderManager.undoLastOrder();
