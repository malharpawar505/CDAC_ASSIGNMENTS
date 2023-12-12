import java.io.IOException;
import java.util.Scanner;

public class ThrowDemo {
    public static void main(String[] args) {
        try {
            Scanner sc = new Scanner(System.in);
            int age = sc.nextInt();
            if (age < 18)
               // throw new RuntimeException()time("Age is below 18 ...Not valid!");
                throw new Exception("Age is below 18 ...Not valid!");
        }
        catch (Exception e)
        {
            System.out.println(e.getMessage());
        }

    }
}
