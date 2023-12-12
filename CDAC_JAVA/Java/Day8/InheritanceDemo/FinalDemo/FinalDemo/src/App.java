public class App {
    public static void main(String[] args) throws Exception {
        System.out.println("Hello, World!");
        //final float PI = 3.14f;
        final float PI;//Blank final variable
        PI = 3.14f;
        System.out.println("Area of Circle = "+ (10*10*PI));
        //PI = 3.145f;
        Car c= new Car();
        System.out.println(c);
         Car c1= new Car(100);
         System.out.println(c1);
    c.applyBreak();
    c1.applyBreak();


    }
}
