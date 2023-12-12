public class Date
{
    private int dd,mm,yy;

    public int getDd() {
        return dd;
    }

    public void setDd(int dd) {
        this.dd = dd;
    }

    public int getMm() {
        return mm;
    }

    public void setMm(int mm) {
        this.mm = mm;
    }

    public int getYy() {
        return yy;
    }

    public void setYy(int yy) {
        this.yy = yy;
    }

    public Date() {
    }

    public Date(int dd, int mm, int yy) {
        this.dd = dd;
        this.mm = mm;
        this.yy = yy;
    }

    @Override
    public String toString() {
        return "Date [dd=" + dd + ", mm=" + mm + ", yy=" + yy + "]";
    }
    
}