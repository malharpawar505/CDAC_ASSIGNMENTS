import java.util.InputMismatchException;
import java.util.Scanner;

// Press Shift twice to open the Search Everywhere dialog and type `show whitespaces`,
// then press Enter. You can now see whitespace characters in your code.
public class Main {
    public static void main(String[] args) {
        try {
            Scanner sc = new Scanner(System.in);
            int no1 = sc.nextInt();
            int no2 = sc.nextInt();
            System.out.println(no1 / no2);
        }catch (InputMismatchException | ArithmeticException e) {
            // e.printStackTrace();
            System.out.println(e.getMessage());
            System.out.println("--------------------");
            System.out.println(e.toString());
        }
        catch (Exception e)
        {
            System.out.println("Arithmatic Exception");
            System.out.println(e.getMessage());
            System.out.println("--------------------");
            System.out.println(e.toString());
        }
       /* catch (InputMismatchException e) {
          // e.printStackTrace();
            System.out.println(e.getMessage());
            System.out.println("--------------------");
            System.out.println(e.toString());
        }*/

        System.out.println("Statement after try and catch");


    }
}