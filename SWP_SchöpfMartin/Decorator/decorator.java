public abstract class decorator implements kaffee {

    protected kaffee coffe;

    public decorator(kaffee coffe) {
        this.coffe = coffe;
    }

    @Override
    public String decorate() {
        return coffe.decorate();
    }

    @Override
    public int price() {
        return coffe.price();  // Get the price from previous decorator/base class
    }
}
