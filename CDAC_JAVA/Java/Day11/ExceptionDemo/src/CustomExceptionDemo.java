import java.util.Scanner;

public class CustomExceptionDemo {
    public static void main(String[] args) throws  InvalidNameException {
        //try {
            Scanner sc = new Scanner(System.in);
            String s = sc.next();

            char[] arr = s.toCharArray();
            if (!(arr[0] >= 'A' && arr[0] <= 'Z'))
                throw new InvalidNameException("First letter is not capital");

            for (int i =1;i<arr.length;i++)
            {
                if(!(arr[i] >='a' && arr[i] <='z'))
                    throw new InvalidNameException(i+" th letter is not small");
            }
            System.out.println("Name is Valid....");


        /*}
        catch(Exception e) {
            System.out.println(e.getMessage());
        }*/



    }
}
