namespace CorePizzaBuilder.entities
{
  public interface IPizzaBuilder
  {
    void SetSize(string size);
    void SetCrustType(string crustType);
    void AddTopping(string topping);
    Pizza GetPizza();
  }
}