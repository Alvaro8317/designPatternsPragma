type State interface {
	orderPizza(*PizzaOrder)
}

type PizzaOrder struct {
	state State
}

func (p *PizzaOrder) setState(state State) {
	p.state = state
}

func (p *PizzaOrder) orderPizza() {
	p.state.orderPizza(p)
}

type PendingState struct{}

func (s *PendingState) orderPizza(order *PizzaOrder) {
	fmt.Println("Su pedido está en espera.")
	order.setState(&PreparingState{})
}

type PreparingState struct{}

func (s *PreparingState) orderPizza(order *PizzaOrder) {
	fmt.Println("Su pizza está en preparación.")
	order.setState(&ReadyState{})
}

type ReadyState struct{}

func (s *ReadyState) orderPizza(order *PizzaOrder) {
	fmt.Println("Su pizza está lista para llevar.")
}

// Ejemplo de uso
func main() {
	order := &PizzaOrder{}
	order.setState(&PendingState{})

	order.orderPizza()
	order.orderPizza()
	order.orderPizza()
}
