import java.util.Scanner;
public class ArrayDemo1
{

  public static void main(String[] args)
{
   Scanner sc = new Scanner(System.in);
   int [] arr = new int[6];

    System.out.println("Please enter " +arr.length +"elements:");

   for(int i=0;i<arr.length;i++)
	arr[i] = sc.nextInt();

System.out.println("\n\n");

   for(int i=0;i<arr.length;i++)
	System.out.print(arr[i] +"\t");
}
}