type Pizza interface {
	prepare()
	bake()
	cut()
	box()
}

type CheesePizza struct{}

func (p *CheesePizza) prepare() {
	fmt.Println("Preparando pizza de queso")
}

func (p *CheesePizza) bake() {
	fmt.Println("Horneando pizza de queso")
}

func (p *CheesePizza) cut() {
	fmt.Println("Cortando pizza de queso")
}

func (p *CheesePizza) box() {
	fmt.Println("Empaquetando pizza de queso")
}

type VeggiePizza struct{}

func (p *VeggiePizza) prepare() {
	fmt.Println("Preparando pizza vegetariana")
}

func (p *VeggiePizza) bake() {
	fmt.Println("Horneando pizza vegetariana")
}

func (p *VeggiePizza) cut() {
	fmt.Println("Cortando pizza vegetariana")
}

func (p *VeggiePizza) box() {
	fmt.Println("Empaquetando pizza vegetariana")
}

func main() {
	cheesePizza := &CheesePizza{}
	veggiePizza := &VeggiePizza{}

	fmt.Println("Haciendo una pizza de queso...")
	cheesePizza.prepare()
	cheesePizza.bake()
	cheesePizza.cut()
	cheesePizza.box()

	fmt.Println("\nHaciendo una pizza vegetariana...")
	veggiePizza.prepare()
	veggiePizza.bake()
	veggiePizza.cut()
	veggiePizza.box()
}
