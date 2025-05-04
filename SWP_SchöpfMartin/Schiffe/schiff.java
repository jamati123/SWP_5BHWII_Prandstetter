import java.util.ArrayList;
import java.util.List;

public interface schiff {
    
    public int länge = 0;
    public boolean vertikal = false;
    public boolean istVersenkt();
    public List<Integer[][]> position = new ArrayList<Integer[][]>();
    public void setPositionV(int x, int y);
    public void setPositionH(int x, int y);
    public boolean checkHit(spielen s);
    


}
