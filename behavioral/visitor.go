type Pizza interface {
	accept(visitor PizzaVisitor)
}

type CheesePizza struct{}

func (p *CheesePizza) accept(visitor PizzaVisitor) {
	visitor.visitCheesePizza(p)
}

type VeggiePizza struct{}

func (p *VeggiePizza) accept(visitor PizzaVisitor) {
	visitor.visitVeggiePizza(p)
}

type PizzaVisitor interface {
	visitCheesePizza(pizza *CheesePizza)
	visitVeggiePizza(pizza *VeggiePizza)
}

type PizzaToppingVisitor struct{}

func (v *PizzaToppingVisitor) visitCheesePizza(pizza *CheesePizza) {
	fmt.Println("Agregando queso a la pizza de queso")
}

func (v *PizzaToppingVisitor) visitVeggiePizza(pizza *VeggiePizza) {
	fmt.Println("Agregando verduras a la pizza vegetariana")
}

func main() {
	cheesePizza := &CheesePizza{}
	veggiePizza := &VeggiePizza{}

	visitor := &PizzaToppingVisitor{}

	cheesePizza.accept(visitor)
	veggiePizza.accept(visitor)
}
