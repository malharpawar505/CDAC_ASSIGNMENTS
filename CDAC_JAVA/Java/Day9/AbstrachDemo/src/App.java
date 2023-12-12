public class App {
    public static void main(String[] args) throws Exception {
        //System.out.println("Hello, World!");
   //int[] arr = new int[3];
   
    Bank[] barr = new Bank[4];
    barr[0]= new SBI();
    barr[1] = new PNB();
    barr[2]=new SubHDFC();
    barr[3]=new SubSubHdfc();

   for (int i = 0; i < barr.length; i++) {
      System.out.println(barr[i].getInterestRate());
   }

    }
}
