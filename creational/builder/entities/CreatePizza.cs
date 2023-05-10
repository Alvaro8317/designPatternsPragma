namespace CorePizzaBuilder.entities
{
  public class Pizza
  {
    public string Size { get; set; }
    public string CrustType { get; set; }
    public List<string> Toppings { get; set; }

    public Pizza()
    {
      Size = "Familiar";
      CrustType = "Square";
      Toppings = new List<string>();
    }

    public void DisplayPizza()
    {
      Console.WriteLine("Size: {0}", Size);
      Console.WriteLine("Crust Type: {0}", CrustType);
      Console.WriteLine("Toppings:");

      foreach (string topping in Toppings)
      {
        Console.WriteLine("- {0}", topping);
      }
    }
  }
}