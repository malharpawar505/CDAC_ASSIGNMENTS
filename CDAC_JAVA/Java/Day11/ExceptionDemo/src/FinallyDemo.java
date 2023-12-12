public class FinallyDemo {
    public static void main(String[] args) {

        try {
            System.out.println("In Program");
            return;
        }catch (Exception e)
        {
            System.out.println(e.toString());
        }
        finally {
            System.out.println("In finally");
        }

        try {
            int no1 = Integer.parseInt(args[0]);
            int no2 = Integer.parseInt(args[1]);
            //int no3 = Integer.parseInt(args[2]);
            System.out.println(no1 / no2);
           // System.exit(0);//no finally executed
            //return ; // Still finally executed

        }
       /* catch (NumberFormatException | ArrayIndexOutOfBoundsException |ArithmeticException e) {
         e.printStackTrace();
        }*/
        finally {
            System.out.println("No matter error occurred or not I will always execute!");
        }

    }
}
