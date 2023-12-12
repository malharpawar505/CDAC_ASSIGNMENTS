class MyThreadClass extends Thread
{
    @Override
    public void run()
    {
        for (int i= 1;i<5;i++) {
            System.out.println(Thread.currentThread().getName() + " : " + i);
            try {
                Thread.sleep(500);
            } catch (InterruptedException e) {
                throw new RuntimeException(e);
            }
        }
    }
}

public class ThreadClassDemo {
    public static void main(String[] args) {
        MyThreadClass t = new MyThreadClass();
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
