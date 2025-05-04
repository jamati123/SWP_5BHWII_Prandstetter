import java.util.ArrayList;
import java.util.List;

public class schlachtschiff implements schiff {
    
    public int länge = 5;
    public spielfeld spielfeld;
    public boolean vertikal;
    public List<Integer[][]> position = new ArrayList<Integer[][]>();

    public boolean istVersenkt() {
        if (position.isEmpty()) {
            System.out.println("Schiff ist versenkt!");
            return true;
        }
        return false;
    }
/* 
    public void setPositionH(int x, int y) {
        while(y + this.länge > 10) {
            y = y - 1;
        }
        this.vertikal = true;
        Integer[][] pos = {{x}, {y}};
        position.add(pos);
        for (int i = 1; i < länge; i++) {
            Integer[][] pos2 = {{x}, {y + 1}};
            position.add(pos2);
        }
    }
*/  

    public schlachtschiff(spielfeld s) {
        this.spielfeld = s;
    }

    public void setPositionH(int x, int y) {
        while(y + this.länge > this.spielfeld.y) {
            y = y - 1;
        }
        this.vertikal = false;
        Integer[][] pos = {{x}, {y}};
        position.add(pos);
        for (int i = 1; i < länge; i++) {
            Integer[][] pos2 = {{x}, {y + i}};
            position.add(pos2);
        }
    }

    public void setPositionV(int x, int y) {
        while(x + this.länge > this.spielfeld.x) {
            x = x - 1;
        }
        this.vertikal = false;
        Integer[][] pos = {{x}, {y}};
        position.add(pos);
        for (int i = 1; i < länge; i++) {
            Integer[][] pos2 = {{x + i}, {y}};
            position.add(pos2);
        }
    }

    public void getPosition() {
        for (Integer[][] pos : position) {
            System.out.println("Position: " + pos[0][0] + ", " + pos[1][0]);
        }
    }


    public boolean checkHit(spielen s) {
        for (Integer[][] pos : position) {
            if (pos[0][0] == s.lastX && pos[1][0] == s.lastY) {
                System.out.println("Hit!");
                position.remove(pos);
                return true;
            }
        }
        System.out.println("Miss!");
        istVersenkt();
        return false;
    }

 // überprüfe ob in einem Radius von 1 ein Schiff ist
    
}

