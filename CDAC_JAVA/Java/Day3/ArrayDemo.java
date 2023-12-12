public class ArrayDemo
{

  public static void main(String[] args)
{
     int[] arr;

    int [] arr1= {1,2,3,4};

    int[] arr2 = new int[5];
     arr2[0] = 10;
     arr2[1]= 20;


    int[] arr3 = new int[]{10,20,30,40};

for(int no:arr1)
  System.out.print(no+"\t");

System.out.println("\n\n__________________________________");

for(int no:arr2)
  System.out.print(no+"\t");


   System.out.println("\n\n__________________________________");

for(int no:arr3)
  System.out.print(no+"\t");

System.out.println("\n\n__________________________________");
System.out.println(arr3[8]);


}

}