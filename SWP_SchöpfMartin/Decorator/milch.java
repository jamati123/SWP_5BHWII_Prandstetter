public class milch extends decorator {

    public milch(kaffee coffe) {
        super(coffe);
    }

    @Override
    public String decorate() {
        return super.decorate() + " " + milchKaffee();
    }

    @Override
    public int price() {
        return super.price() + milchPreis();  // Add price of sugar each time
    }

    public String milchKaffee() {
        return "lecka milch";
    }

    public int milchPreis() {
        return 4;  // Fixed price of sugar
    }
}
