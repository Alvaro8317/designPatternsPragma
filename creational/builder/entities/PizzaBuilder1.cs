namespace CorePizzaBuilder.entities
{
  public class PizzaBuilder : IPizzaBuilder
  {
    private Pizza pizza;

    public PizzaBuilder()
    {
      pizza = new Pizza();
    }

    public void SetSize(string size)
    {
      pizza.Size = size;
    }

    public void SetCrustType(string crustType)
    {
      pizza.CrustType = crustType;
    }

    public void AddTopping(string topping)
    {
      pizza.Toppings.Add(topping);
    }

    public Pizza GetPizza()
    {
      return pizza;
    }
  }
}