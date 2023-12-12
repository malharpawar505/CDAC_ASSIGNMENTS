public class Numbers {
        public static void main(String[] args) {
//        Thread t = new Thread();
//        t.start();
            System.out.println("In main thread");
            for (int i=1;i<=5;i++)
            {
                System.out.println(Thread.currentThread().getName() + " : " + i);
                try {
                    Thread.sleep(500);
                }catch(Exception ex) {
                    System.out.println("Exception");
                }
            }
        }
    }

