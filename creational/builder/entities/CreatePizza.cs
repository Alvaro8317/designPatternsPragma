namespace CorePizzaBuilder.entities
{
  class CreatePizza
  {
    public interface IBuilder
    {
      void CreateMass();
      void MakeToppings();
      void ThrowCheese();
      void MakePizza();
    }
  }
}