public class Car extends Vehicle {
    private int speed;
    final int speedlimit;
    //Instance initialiser bloack
    {
        System.out.println("In InInitialiser Block");
      speed = 60;
      speedlimit = 160;
    }
    public Car(int speed) {
        System.out.println("In Parametrised Constructor");
        this.speed = speed;
    }
    public Car() {
        System.out.println("In Default Constructor");
    }
    @Override
    public String toString() {
        return "Car [speed=" + speed + "speedlimit= "+speedlimit+ "]";
    }


    //Can not override Final method
    /*public void applyBreak()
    {
      System.out.println("ABS Breaks are applied..");
    }*/
}
