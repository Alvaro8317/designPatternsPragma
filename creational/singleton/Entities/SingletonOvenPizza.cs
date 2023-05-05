using static System.Console;

namespace CorePizzaSingleton.Entities
{
    public sealed class SingletonOvenPizza
    {
        private static SingletonOvenPizza _instance;

        // Private constructor
        private SingletonOvenPizza()
        {
            WriteLine("Creating an oven!");
        }

        // Static prop to get the instance
        public static SingletonOvenPizza Instance
        {
            get
            {
                if (_instance == null)
                {
                    WriteLine("The instance is null! I'm going to create one single Oven!");
                    _instance = new SingletonOvenPizza();
                }
                return _instance;
            }
        }

        public void MakePizza()
        {
            WriteLine("Making a pizza!");
        }
    }
}
