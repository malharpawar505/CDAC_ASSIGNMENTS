public class App {
    public static void main(String[] args) throws Exception {
        System.out.println("Hello, World!");
       Test t = new Test();
       t.draw();
       t.msg();
       t.msg1();
       Drawable t1 = new Test();
       Drawable.statMethod();
       t1.draw();
       t1.msg();
       ((Test)t1).msg1();
   
    }
}
