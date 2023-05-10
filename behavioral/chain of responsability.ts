// Interfaz Handler que define el método para manejar un pedido de pizza
interface Handler {
  setNext(handler: Handler): Handler;
  handle(request: PizzaRequest): void;
}

// Clase AbstractHandler que implementa Handler y define el método setNext
abstract class AbstractHandler implements Handler {
  private nextHandler: Handler | null = null;

  setNext(handler: Handler): Handler {
    this.nextHandler = handler;
    return handler;
  }

  handle(request: PizzaRequest): void {
    if (this.nextHandler) {
      this.nextHandler.handle(request);
    }
  }
}

// Clase OrderHandler que maneja los pedidos y los envía al siguiente handler si es necesario
class OrderHandler extends AbstractHandler {
  handle(request: PizzaRequest): void {
    console.log('Manejando pedido...');
    if (request.order === 'Pizza Margherita') {
      console.log('Preparando Pizza Margherita');
    } else {
      super.handle(request);
    }
  }
}

// Clase StockHandler que maneja los ingredientes disponibles y los envía al siguiente handler si es necesario
class StockHandler extends AbstractHandler {
  handle(request: PizzaRequest): void {
    console.log('Verificando stock...');
    if (request.ingredient === 'tomate' && request.amount > 0) {
      console.log('Tomates disponibles');
    } else {
      super.handle(request);
    }
  }
}

// Clase DeliveryHandler que maneja la entrega y los envía al siguiente handler si es necesario
class DeliveryHandler extends AbstractHandler {
  handle(request: PizzaRequest): void {
    console.log('Preparando entrega...');
    if (request.address === '123 Calle Falsa') {
      console.log('Entrega a 123 Calle Falsa');
    } else {
      super.handle(request);
    }
  }
}

// Clase PizzaRequest que encapsula la información de un pedido de pizza
class PizzaRequest {
  public order: string;
  public ingredient: string;
  public amount: number;
  public address: string;

  constructor(
    order: string,
    ingredient: string,
    amount: number,
    address: string
  ) {
    this.order = order;
    this.ingredient = ingredient;
    this.amount = amount;
    this.address = address;
  }
}

// Ejemplo de uso
const orderHandler = new OrderHandler();
const stockHandler = new StockHandler();
const deliveryHandler = new DeliveryHandler();

orderHandler.setNext(stockHandler).setNext(deliveryHandler);

const request1 = new PizzaRequest('Pizza Margherita', '', 0, '');
const request2 = new PizzaRequest('Pizza de Peperoni', 'tomate', 1, '');
const request3 = new PizzaRequest(
  'Pizza de Champiñones',
  'tomate',
  0,
  '123 Calle Falsa'
);

orderHandler.handle(request1);
orderHandler.handle(request2);
orderHandler.handle(request3);
