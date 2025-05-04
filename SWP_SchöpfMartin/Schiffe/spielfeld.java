

public class spielfeld implements Observer {


    public int[][] spielfeld;
    public int x;
    public int y;
    
    public spielfeld(int x, int y) {
        this.x = x;
        this.y = y;
        this.spielfeld = new int[x][y]; // 10x10 Spielfeld
    }

    public void spielfeldErstellen() {
        for (int i = 0; i < this.x; i++) {
            for (int j = 0; j < this.y; j++) {
                spielfeld[i][j] = 0;
            }
        }
    }

    public void spielfeldAusgeben() {
        System.out.println("Spielfeld:");
        for (int i = 0; i < this.x; i++) {
            for (int j = 0; j < this.y; j++) {
                System.out.print(spielfeld[i][j] + " ");
            }
            System.out.println();
        }
    }

    public void setOnPosition(int x, int y, int value) {
        if (x >= 0 && x < this.x && y >= 0 && y < this.y) {
            spielfeld[x][y] = value;
        } else {
            System.out.println("Ungültige Position!");
        }
    }

    public void update(spielen s) {
       if (s.wasHit) {
            System.out.println("Hit at position: " + s.lastX + ", " + s.lastY);
            setOnPosition(s.lastX, s.lastY, 8); // Mark hit on the field
        } else if(!s.wasHit) {
            setOnPosition(s.lastX, s.lastY, 1); // Mark Miss
        }
    }

   
}