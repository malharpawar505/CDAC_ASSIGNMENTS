import java.util.Scanner;
public class InputDemo{
    public static void main(String[] args)
{
   System.out.println("Welcome");
    Scanner sc = new Scanner(System.in);
    System.out.println("Enter no");
     int  no = sc.nextInt();
     System.out.println("Enter marks");
     float marks = sc.nextFloat();
     System.out.println("Enter Name");
     String  name = sc.next();
     System.out.println("Enter Gender");
     char  gender = sc.next().charAt(0);

   System.out.println(no + "  "+ name + "  "+ marks +"  " +gender);  

}
 
}