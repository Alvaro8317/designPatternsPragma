type Observer interface {
	update(subject Subject)
}

type Subject interface {
	attach(observer Observer)
	detach(observer Observer)
	notify()
}

type PizzaOrder struct {
	observers []Observer
}

func (p *PizzaOrder) attach(observer Observer) {
	p.observers = append(p.observers, observer)
}

func (p *PizzaOrder) detach(observer Observer) {
	for i, o := range p.observers {
			if o == observer {
					p.observers = append(p.observers[:i], p.observers[i+1:]...)
					break
			}
	}
}

func (p *PizzaOrder) notify() {
	for _, observer := range p.observers {
			observer.update(p)
	}
}

type Customer struct{}

func (c *Customer) update(subject Subject) {
	fmt.Println("¡Su pedido de pizza está listo!")
}

// Ejemplo de uso
func main() {
	order := &PizzaOrder{}
	customer := &Customer{}

	order.attach(customer)

	order.notify()
}
