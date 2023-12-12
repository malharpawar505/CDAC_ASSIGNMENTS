public interface MydemoInterface {
    double PI =3.14;
    void display();
  static void calculateArea(int radius)
  {
   System.out.println(radius*radius*PI);
  }

   default void calculateCircumfarance(int radius)
  {
   System.out.println(2*radius*PI);
  }

}

class MyTest implements MydemoInterface
{
  public void display()
  {
    System.out.println("In Display method");
  }

  public void mytestOwnMethod()
  {
    System.out.println("In mytestOwnMethod method");
  }

}

class MyTestDemo 
{
    public static void main(String[] args) {
        MyTest t = new MyTest();
        t.calculateCircumfarance(10);
        t.display();
       // t.calculateArea(); not Available
       MydemoInterface.calculateArea(20);
       t.mytestOwnMethod();


       MydemoInterface t1 = new MyTest();
       t1.display();
       t1.calculateCircumfarance(3);
       MydemoInterface.calculateArea(5);
       //t1.mytestOwnMethod(); error
       ((MyTest)t1).mytestOwnMethod();
    }
}
