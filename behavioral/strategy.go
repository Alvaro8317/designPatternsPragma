type PaymentStrategy interface {
	pay(amount float64)
}

type CreditCardStrategy struct{}

func (s *CreditCardStrategy) pay(amount float64) {
	fmt.Printf("Pagando %.2f con tarjeta de crédito\n", amount)
}

type PayPalStrategy struct{}

func (s *PayPalStrategy) pay(amount float64) {
	fmt.Printf("Pagando %.2f con PayPal\n", amount)
}

type PaymentContext struct {
	paymentStrategy PaymentStrategy
}

func (c *PaymentContext) setPaymentStrategy(paymentStrategy PaymentStrategy) {
	c.paymentStrategy = paymentStrategy
}

func (c *PaymentContext) makePayment(amount float64) {
	c.paymentStrategy.pay(amount)
}

func main() {
	context := &PaymentContext{}

	creditCardStrategy := &CreditCardStrategy{}
	payPalStrategy := &PayPalStrategy{}

	context.setPaymentStrategy(creditCardStrategy)
	context.makePayment(50.00)

	context.setPaymentStrategy(payPalStrategy)
	context.makePayment(100.00)
}
