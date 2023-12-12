import java.util.Scanner;

public class App {
    public static void main(String[] args) throws Exception {
        //System.out.println("Hello, World!");
        Scanner sc = new Scanner(System.in);       Customer[] carr= new Customer[5];
        for (int i = 0; i < carr.length; i++) {
            System.out.println("Enter choice, name and address");
            char choice = sc.next().charAt(0);
            String nm = sc.next();
            String ad = sc.next();
            int rno=0;
            if(choice =='r')
            {
                System.out.println("Enter reg no:");
                rno = sc.nextInt();
                carr[i]= new RegCustomer(nm, ad, rno);
            }
            else
            carr[i]= new Customer(nm, ad);
   

        }

        for (int i = 0; i < carr.length; i++) {
            System.out.println(carr[i]);
            System.out.println(carr[i].getDiscount(5000));
        }
        


    }
}
