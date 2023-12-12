class PrintNumber
{
    //public synchronized void printTableOfNumber(int no)
    public  void printTableOfNumber(int no) //either used at Method level or Block level
    {
        synchronized(this) { //Object level
            for (int i = 1; i < 11; i++) {
                System.out.println(Thread.currentThread().getName() + ": " + i * no);
            }
        }
    }
}

class Thread1 extends Thread
{
    PrintNumber p;
    public Thread1(PrintNumber pobj)
    {
        this.p = pobj;
    }

    @Override
    public void run()
    {
        p.printTableOfNumber(12);
    }

}

class Thread2 extends Thread
{
    PrintNumber p;
    public Thread2(PrintNumber pobj)
    {
        this.p = pobj;
    }

    @Override
    public void run()
    {
        p.printTableOfNumber(15);
    }

}

public class ThreadSynchronisationDemo {
    public static void main(String[] args) {
        PrintNumber p = new PrintNumber();
        Thread1 t1 = new Thread1(p);
        Thread2 t2 = new Thread2(p);

        t1.start();
        t2.start();



    }
}
