class MyRunnableClass implements Runnable
{
    @Override
    public void run()
    {
        for (int i= 1;i<20;i++) {
            System.out.println(Thread.currentThread().getName() + " : " + i);
            try {
                Thread.sleep(500);
            } catch (InterruptedException e) {
                throw new RuntimeException(e);
            }
        }
    }
}

public class RunnableDemo {
    public static void main(String[] args) {
        Runnable r = new MyRunnableClass();
        Thread t = new Thread(r); //Passing Runnable ref as Start method is not with Runnable Interface
        t.start();


        System.out.println("Main Thread");
        for(int i = 10;i<200;i=i+10) {
            System.out.println(Thread.currentThread().getName() + " : " + i);
            try {
                Thread.sleep(500);
            }catch(Exception ex) {
                System.out.println("Exception");
            }
        }
    }
}
