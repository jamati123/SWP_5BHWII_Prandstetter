public class Main {
    public static void main(String[] args) {
        kaffee simpleKaffee = new implementsKaffee();
        System.out.println(simpleKaffee.decorate() + " Price: " + simpleKaffee.price());

        kaffee zuckerKaffee = new zucker(simpleKaffee);
        System.out.println(zuckerKaffee.decorate() + " Price: " + zuckerKaffee.price());

        kaffee milchKaffee = new milch(simpleKaffee);
        System.out.println(milchKaffee.decorate() + " Price: " + milchKaffee.price());

        kaffee milchZucker = new milch(zuckerKaffee);
        System.out.println(milchZucker.decorate() + " Price: " + milchZucker.price());

        kaffee milchZuckerSuess = new suesstoff(milchZucker);
        System.out.println(milchZuckerSuess.decorate() + " Price: " + milchZuckerSuess.price());


        
    }
}
