class Account
{
    int bal;
    public Account()
    {
        this.bal = 1000;
    }

    public synchronized void withdraAmount(int amt) throws InterruptedException {
        System.out.println("I am withdrawing amt....");
        if(this.bal - amt <1000)
        {
            System.out.println("Insufficient Balance you can not withdraw....");
            wait();
        }
        this.bal -=amt;
        System.out.println("Amount withdraw successfully... "+this.bal);

    }

    public synchronized void deposit(int amt)
    {
        System.out.println("I am depositing ...");
        this.bal +=amt;
        System.out.println("Amount deposited successfully...."+this.bal);
        notify();
    }

}


class Thread11 extends Thread
{
    Account acc;
    public Thread11(Account pobj)
    {
        this.acc = pobj;
    }

    @Override
    public void run()
    {
        try {
            acc.withdraAmount(800);
        } catch (InterruptedException e) {
            throw new RuntimeException(e);
        }
    }

}

class Thread21 extends Thread
{
    Account acc;
    public Thread21(Account pobj)
    {
        this.acc = pobj;
    }

    @Override
    public void run()
    {
        acc.deposit(1000);
    }

}

public class ThreadCommunicationDemo {
    public static void main(String[] args) throws InterruptedException {
        Account acc = new Account();
        Thread11 t1 = new Thread11(acc);
        Thread21 t2 = new Thread21(acc);
        t1.start();
        Thread.sleep(500);
        t2.start();
    }


}
