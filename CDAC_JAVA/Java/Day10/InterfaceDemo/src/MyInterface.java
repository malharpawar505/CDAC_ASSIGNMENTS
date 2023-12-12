 interface MyInterface {
   void method1();
   void method2();
}


interface MyInterface1 {
   void method3();
   void method4();
}

class Myclass implements MyInterface,MyInterface1{
    public void method1()
    {
        System.out.println("In Method1");
    }
    public void method2()
    {
        System.out.println("In Method2");
    }
    public void method3()
    {
        System.out.println("In Method3");
    }
    public void method4()
    {
        System.out.println("In Method4");
    }


}

class MyClassDemo{

    public static void main(String[] args) {
        Myclass m = new Myclass();
        m.method1();
        m.method2();
        m.method3();
        m.method4();

        MyInterface m1 = new Myclass();
        m1.method1();
        m1.method2();
        //m1.method3();
        //m1.method4();


        MyInterface1 m2 = new Myclass();
        //m2.method1();
        //m2.method2();
        m2.method3();
        m2.method4();

        if( m instanceof Myclass)
            System.out.println("m is Myclass");

        if( m1 instanceof Myclass)
            System.out.println("m is Myclass");

        if( m2 instanceof Myclass)
            System.out.println("m is Myclass");




    }
}