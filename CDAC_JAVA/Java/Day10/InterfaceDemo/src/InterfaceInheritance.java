interface A{
    void method1();
    void method2();
}

interface B{
    void method3();
    void method4();
}

interface C extends A,B{ 
    void method5();
}

abstract class InheritanceDemo implements C{

    @Override
    public void method1() {
        System.out.println("method1");
         }

    @Override
    public void method2() {
         System.out.println("method2");
         }

    @Override
    public void method3() {
         System.out.println("method4");
          }

    
}
