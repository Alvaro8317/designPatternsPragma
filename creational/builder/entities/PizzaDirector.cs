namespace CorePizzaBuilder.entities
{
  public class PizzaDirector
  {
    public Pizza BuildPizza(IPizzaBuilder pizzaBuilder)
    {
      pizzaBuilder.SetSize("Medium");
      pizzaBuilder.SetCrustType("Thin");
      pizzaBuilder.AddTopping("Mushrooms");
      pizzaBuilder.AddTopping("Onions");
      pizzaBuilder.AddTopping("Peppers");

      return pizzaBuilder.GetPizza();
    }
  }
}