type Iterator interface {
	hasNext() bool
	next() interface{}
}

// Clase PizzaOrder que representa un pedido de pizza
type PizzaOrder struct {
	name string
	toppings []string
}

// Clase PizzaOrderCollection que representa una colección de pedidos de pizza
type PizzaOrderCollection struct {
	orders []*PizzaOrder
}

// Clase PizzaOrderIterator que implementa Iterator y recorre la colección de pedidos de pizza
type PizzaOrderIterator struct {
	collection *PizzaOrderCollection
	index int
}

func (i *PizzaOrderIterator) hasNext() bool {
	return i.index < len(i.collection.orders)
}

func (i *PizzaOrderIterator) next() interface{} {
	if !i.hasNext() {
			return nil
	}
	order := i.collection.orders[i.index]
	i.index++
	return order
}

// Método para agregar un pedido de pizza a la colección
func (c *PizzaOrderCollection) addOrder(order *PizzaOrder) {
	c.orders = append(c.orders, order)
}

// Ejemplo de uso
func main() {
	collection := &PizzaOrderCollection{}

	order1 := &PizzaOrder{name: "Pizza Margherita", toppings: []string{"Tomate", "Queso"}}
	order2 := &PizzaOrder{name: "Pizza Pepperoni", toppings: []string{"Tomate", "Queso", "Pepperoni"}}
	order3 := &PizzaOrder{name: "Pizza Hawaiana", toppings: []string{"Tomate", "Queso", "Piña", "Jamón"}}

	collection.addOrder(order1)
	collection.addOrder(order2)
	collection.addOrder(order3)

	iterator := &PizzaOrderIterator{collection: collection}

	for iterator.hasNext() {
			order := iterator.next().(*PizzaOrder)
			fmt.Printf("%s - Ingredientes: %v\n", order.name, order.toppings)
	}
}
