public interface Pizza {
    void prepare();
    void bake();
    void cut();
    void box();
}

interface PizzaFactory {
    CheesePizza createCheesePizza();
    VeggiePizza createVeggiePizza();
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
        System.out.println("Empaquetando pizza de
 abstract factory {
  
}
