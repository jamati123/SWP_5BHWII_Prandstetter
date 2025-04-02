public class zucker extends decorator {

    public zucker(kaffee coffe) {
        super(coffe);
    }

    @Override
    public String decorate() {
        return super.decorate() + " " + zuckerKaffee();
    }

    @Override
    public int price() {
        return super.price() + zuckerPreis();  // Add price of sugar each time
    }

    public String zuckerKaffee() {
        return "lecka zucka";
    }

    public int zuckerPreis() {
        return 5;  // Fixed price of sugar
    }
}
