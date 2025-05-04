import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import java.util.Random;

public class spielen {
    
    public int lastX = 0;
    public int lastY = 0;
    public boolean wasHit = false;

    private List<spielfeld> spielfelder = new ArrayList<spielfeld>();
    private List<schiff> schiffe = new ArrayList<schiff>();


    public void notify(List<spielfeld> spielfelder) {
        for (spielfeld s : spielfelder) {
            s.update(this);
        }
    }

    public void notifySchiff(List<schiff> schiffe) {
        for (schiff s : schiffe) {
            boolean check = s.checkHit(this);
            if (check) {
                this.wasHit = true;
                return;
            } else {
                this.wasHit = false;
            }
        }
    }
    
    public boolean checkWin() {
        int count = 0;
        for (schiff s : schiffe) {
            if (s.istVersenkt()) {

            } else {
                count++;
            }
        }
        if (count == 0) {
            System.out.println("Alle Schiffe versenkt!");
            return true;
        } else {
            System.out.println("Es sind noch Schiffe übrig!");
            return false;
        }
    }

    public void setLastX(int x) {
        this.lastX = x;
    }

    public void setLastY(int y) {
        this.lastY = y;
    }

    public void addSpielfeld(spielfeld s) {
        spielfelder.add(s);
    }

    /* 
    public boolean checkSpace(schiff newSchiff) {

        for (schiff existingSchiff : schiffe) {
                for (Integer[][] pos : existingSchiff.position) {
                    for (Integer[][] newPos : newSchiff.position) {
                        if (pos[0][0] == newPos[0][0] && pos[1][0] == newPos[1][0]) {
                            System.out.println("Platz ist belegt!");
                            return false;
                        }
                    }
                }
            }
         

        return true;
    } */

    public void setSchiff(schiff s) {
        this.schiffe.add(s);
    }

    public spielen(spielfeld spielfeld) {
        spielfeld.spielfeldErstellen();
        spielfelder.add(spielfeld);
    }

    public void solve() {
        spielfeld s = this.spielfelder.get(0);

        for (int i = 0; i < s.x; i++) {
            for (int j = 0; j < s.y; j++) {
                System.out.print(s.spielfeld[i][j] + " ");
                setLastX(i);
                setLastY(j);
                this.notifySchiff(this.schiffe);
                this.notify(this.spielfelder);
            }
            s.spielfeldAusgeben();
            System.out.println();
        }
    }
    
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);
        Random rand = new Random();
        spielfeld spielfeld = new spielfeld(10, 10);
        spielfeld.spielfeldErstellen();
        spielfeld.spielfeldAusgeben();

        schlachtschiff schiff1 = new schlachtschiff(spielfeld);
        schiff1.setPositionH(2, 3);
        schiff1.getPosition();

        spielen spiel = new spielen(spielfeld);
        spiel.addSpielfeld(spielfeld);
        spiel.setSchiff(schiff1);


        schlachtschiff schiff2 = new schlachtschiff(spielfeld);        
        schiff2.setPositionV(4, 5);
        spiel.setSchiff(schiff2);
        
        schlachtschiff schiff3 = new schlachtschiff(spielfeld);
        schiff3.setPositionV(8, 8);
        spiel.setSchiff(schiff3);


       
        // spiel.solve(); // Löst das Spiel und gibt die Positionen aus

        spiel.solve();


        while (!spiel.checkWin()) {
            System.out.println("Geben Sie die X-Position ein (0-9): ");
            int x = scanner.nextInt();
            spiel.setLastX(x);
            System.out.println("Geben Sie die Y-Position ein (0-9): ");
            int y = scanner.nextInt();
            spiel.setLastY(y);

            spiel.notifySchiff(spiel.schiffe);
            spiel.notify(spiel.spielfelder);

            spielfeld.spielfeldAusgeben();
            System.out.println("--------------------------------");
            System.out.println("1 - Miss / 2 - Hit");
            
        }


        
    }
}
