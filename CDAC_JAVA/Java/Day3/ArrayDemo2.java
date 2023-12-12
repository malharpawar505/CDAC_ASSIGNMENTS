import java.util.Scanner;
public class ArrayDemo2
{

  public static void main(String[] args)
{
   Scanner sc = new Scanner(System.in);
   int[][] arr= {{1,2},{5,8},{7,9}};
System.out.println(arr.length);
   for(int i = 0;i<3;i++)
{
	for(int j = 0;j<2;j++)
	System.out.print( arr[i][j] +"\t");
System.out.println();

}

System.out.println("\n=============================");
for(int[] a: arr)
{
   for(int n:a)
    System.out.print(n +"\t");
System.out.println();
}

//Accept from User
int[][] arr2= new int [3][3];
System.out.println("Enter array ele:");
for(int i = 0;i<3;i++)
{
	for(int j = 0;j<3;j++)
	arr2[i][j] = sc.nextInt();


}

//Print values
for(int i = 0;i<3;i++)
{
	for(int j = 0;j<3;j++)
	System.out.print( arr2[i][j] +"\t");
System.out.println();

}


}
}