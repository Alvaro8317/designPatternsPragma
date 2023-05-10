import java.util.HashMap;
import java.util.Map;

abstract class Pizza implements Cloneable {
    private String name;
    private String dough;
    private String sauce;
    private String toppings;

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getDough() {
        return dough;
    }

    public void setDough(String dough) {
        this.dough = dough;
    }

    public String getSauce() {
        return sauce;
    }

    public void setSauce(String sauce) {
        this.sauce = sauce;
    }

    public String getToppings() {
        return toppings;
    }

    public void setToppings(String toppings) {
        this.toppings = toppings;
    }

    public abstract Pizza clone();
}

class CheesePizza extends Pizza {
    public CheesePizza() {
        setName("Pizza de queso");
        setDough("Masa delgada");
        setSauce("Salsa de tomate");
        setToppings("Queso mozzarella");
    }

    public Pizza clone() {
        return new CheesePizza();
    }
}

class VeggiePizza extends Pizza {
    public VeggiePizza() {
        setName("Pizza vegetariana");
        setDough("Masa gruesa");
        setSauce("Salsa de tomate");
        setToppings("Pimiento, cebolla, champiñones");
    }

    public Pizza clone() {
        return new VeggiePizza();
    }
}

class PizzaStore {
    private static Map<String, Pizza> prototypes = new HashMap<>();

    static {
        prototypes.put("cheese", new CheesePizza());
        prototypes.put("veggie", new VeggiePizza());
    }

    public static Pizza orderPizza(String type) throws CloneNotSupportedException {
        Pizza pizza = prototypes.get(type).clone();
        System.out.println("Se ha ordenado una pizza " + pizza.getName());
        return pizza;
    }
}

public class Prototype {
    public static void main(String[] args) throws CloneNotSupportedException {
        Pizza cheesePizza = PizzaStore.orderPizza("cheese");

        Pizza veggiePizza = PizzaStore.orderPizza("veggie");
    }
}
