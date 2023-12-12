class Mythread extends Thread
{
    int no;

    public Mythread() {
        this.no = 10;
    }
    public Mythread(int num) {
        this.no=num;
    }

    @Override
    public void run() {
        for (int i = no;i>0;i--) {
            System.out.println(Thread.currentThread().getName() + ":" + i);
            try {
                Thread.sleep(200);
            } catch (InterruptedException e) {
                throw new RuntimeException(e);
            }
        }
    }
}


public class MultipleThreadDemo {
    public static void main(String[] args) throws InterruptedException {
        Mythread t = new Mythread();
        Mythread t1 = new Mythread(20);
        Mythread t2 = new Mythread(50);

        t.start();
        t1.start();
        t2.start();

        System.out.println("In Main Method");
        for(int i=10;i<100;i=i+10) {
            System.out.println(Thread.currentThread().getName() + ": " + i);
            Thread.sleep(200);
        }

        t.join();
        t1.join();
        t2.join();
        System.out.println("All Tasks are Completed....");
    }

}
