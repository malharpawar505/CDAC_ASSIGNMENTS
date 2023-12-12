
//This is Single line Comment
/*This 
is  
Multiline*/

/**
*This is my class which prints Range of Prime no
*/
public class PrintPrime
{

/**
*This is my main method where I  have wriiten logic
*/
   public static void main(String[] args)
{
   for(int no = 11; no<=100;no++)
{
	boolean flag= true;
    for(int i =2;i<no;i++)
   {
      if(no%i ==0)
	{
    	flag= false;
    	break;
	}//if
    }//for
  if(flag)
    System.out.println(no+" is prime");

}//1st for
}
}