public class implementsKaffee implements kaffee {

    private int currentPrice = 5; 

    @Override
    public String decorate() {
        return "Kaffee";
    }

    @Override
    public int price() {
        return this.currentPrice;
    }
}
