public class Main {
    public static void main(String[] args) {
        kaffee simpleKaffee = new implementsKaffee();
        System.out.println(simpleKaffee.decorate() + " Preis: " + simpleKaffee.price());

        kaffee zuckerKaffee = new zucker(simpleKaffee);
        System.out.println(zuckerKaffee.decorate() + " Preis: " + zuckerKaffee.price());

        kaffee milchKaffee = new milch(simpleKaffee);
        System.out.println(milchKaffee.decorate() + " Preis: " + milchKaffee.price());

        kaffee milchZucker = new milch(zuckerKaffee);
        System.out.println(milchZucker.decorate() + " Preis: " + milchZucker.price());

        kaffee milchZuckerSuess = new suesstoff(milchZucker);
        System.out.println(milchZuckerSuess.decorate() + " Preis: " + milchZuckerSuess.price());


        
    }
}
