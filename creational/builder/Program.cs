using CorePizzaBuilder.entities;

namespace CorePizzaBuilder
{
  public class Program
  {
    PizzaDirector director = new PizzaDirector();
    PizzaBuilder builder = new PizzaBuilder();

    static void Main(string[] args)
    {
      PizzaDirector director = new PizzaDirector();
      PizzaBuilder builder = new PizzaBuilder();

      Pizza pizza = director.BuildPizza(builder);
      pizza.DisplayPizza();
    }

  }
}
