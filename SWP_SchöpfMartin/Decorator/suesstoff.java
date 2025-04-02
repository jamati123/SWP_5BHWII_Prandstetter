public class suesstoff extends decorator {

    public suesstoff(kaffee coffe) {
        super(coffe);
    }

    @Override
    public String decorate() {
        return super.decorate() + " " + suesstoffKaffee();
    }

    @Override
    public int price() {
        return super.price() + suesstoffPreis();  // Add price of sugar each time
    }

    public String suesstoffKaffee() {
        return "lecka suesstoff";
    }

    public int suesstoffPreis() {
        return 3;  // Fixed price of sugar
    }
}
