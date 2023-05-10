interface Pizza {
    void prepare();
    void bake();
    void cut();
    void box();
}

class CheesePizza implements Pizza {
    public void prepare() {
        System.out.println("Preparando pizza de queso");
    }

    public void bake() {
        System.out.println("Horneando pizza de queso");
    }

    public void cut() {
        System.out.println("Cortando pizza de queso");
    }

    public void box() {
        System.out.println("Empaquetando pizza de queso");
    }
}

class VeggiePizza implements Pizza {
    public void prepare() {
        System.out.println("Preparando pizza vegetariana");
    }

    public void bake() {
        System.out.println("Horneando pizza vegetariana");
    }

    public void cut() {
        System.out.println("Cortando pizza vegetariana");
    }

    public void box() {
        System.out.println("Empaquetando pizza vegetariana");
    }
}

class PizzaFactory {
    public Pizza createPizza(String type) {
        if (type.equals("cheese")) {
            return new CheesePizza();
        } else if (type.equals("veggie")) {
            return new VeggiePizza();
        } else {
            throw new IllegalArgumentException("Tipo de pizza inválido");
        }
    }
}

class PizzaStore {
    private PizzaFactory factory;

    public PizzaStore(PizzaFactory factory) {
        this.factory = factory;
    }

    public Pizza orderPizza(String type) {
        Pizza pizza = factory.createPizza(type);
        pizza.prepare();
        pizza.bake();
        pizza.cut();
        pizza.box();
        return pizza;
    }
}

public class Main {
    public static void main(String[] args) {
        PizzaFactory factory = new PizzaFactory();
        PizzaStore store = new PizzaStore(factory);

        Pizza cheesePizza = store.orderPizza("cheese");
        System.out.println("Se ha ordenado una pizza de queso");

        Pizza veggiePizza = store.orderPizza("veggie");
        System.out.println("Se ha ordenado una pizza vegetariana");
    }
}
