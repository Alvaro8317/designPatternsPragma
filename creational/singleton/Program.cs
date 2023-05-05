/* 
* 1. Make the default constructor private, to prevent other objects from using the new operator with the Singleton class.
* 2. Create a static creation method that acts as a constructor. Under the hood, this method calls the private constructor to create an object and saves it in a static field. All following calls to this method return the cached object.
*/
using static System.Console;
using CorePizzaSingleton.Entities;

namespace CorePizzaSingleton
{
  class Program
  {
    public static void Main()
    {
      WriteLine("Welcome to my pizza restaurant!");
      /* It doesn't create an instance like other classes, it calls the method getInstance */
      SingletonOvenPizza pizzaOven = SingletonOvenPizza.Instance;
      SingletonOvenPizza pizzaOven2 = SingletonOvenPizza.Instance;
      WriteLine($"Is the same instance? {pizzaOven == pizzaOven2}");
      ReadLine(); //! Enter to finish the program
      WriteLine("Goodbye!");
    }
  }
}