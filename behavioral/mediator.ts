interface Mediator {
  notify(sender: any, event: string): void;
}

class PizzaMediator implements Mediator {
  private customer: Customer;
  private chef: Chef;
  private delivery: Delivery;

  setCustomer(customer: Customer) {
    this.customer = customer;
  }

  setChef(chef: Chef) {
    this.chef = chef;
  }

  setDelivery(delivery: Delivery) {
    this.delivery = delivery;
  }

  notify(sender: any, event: string) {
    if (event === "order") {
      this.chef.preparePizza(sender);
    } else if (event === "ready") {
      this.delivery.deliverPizza(sender);
    } else if (event === "delivered") {
      this.customer.receivePizza(sender);
    }
  }
}

class Pizza {
  constructor(private name: string) {}

  getName() {
    return this.name;
  }
}

class Customer {
  constructor(private mediator: Mediator) {}

  orderPizza(pizza: Pizza) {
    console.log("El cliente ha ordenado una pizza " + pizza.getName());
    this.mediator.notify(pizza, "order");
  }

  receivePizza(pizza: Pizza) {
    console.log("El cliente ha recibido su pizza " + pizza.getName());
  }
}

class Chef {
  constructor(private mediator: Mediator) {}

  preparePizza(pizza: Pizza) {
    console.log("El chef está preparando una pizza " + pizza.getName());
    setTimeout(() => {
      console.log("La pizza " + pizza.getName() + " está lista");
      this.mediator.notify(pizza, "ready");
    }, 3000);
  }
}

class Delivery {
  constructor(private mediator: Mediator) {}

  deliverPizza(pizza: Pizza) {
    console.log("El repartidor está entregando la pizza " + pizza.getName());
    setTimeout(() => {
      console.log("La pizza " + pizza.getName() + " ha sido entregada");
      this.mediator.notify(pizza, "delivered");
    }, 5000);
  }
}

const mediator = new PizzaMediator();

const pizza = new Pizza("Hawaiana");
const customer = new Customer(mediator);
const chef = new Chef(mediator);
const delivery = new Delivery(mediator);

mediator.setCustomer(customer);
mediator.setChef(chef);
mediator.setDelivery(delivery);

customer.orderPizza(pizza);
