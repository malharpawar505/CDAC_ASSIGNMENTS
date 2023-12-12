public class CmdDemo
{

  public static void main(String[] args)
{
int []arr = new int[3];
   for (String s:args)
{
System.out.println(s);

}

for (int i= 0; i<3;i++)
{
  arr[i] = Integer.parseInt(args[i]);
}

for(int a: arr)
  System.out.println(a);


}

}