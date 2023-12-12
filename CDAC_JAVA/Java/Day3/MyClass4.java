class Date
{
  private int dd,mm,yy;
  public showDate()
	{
 	System.out.println(dd+"-"+mm+"-"+yy);
	} 
}

public class MyClass4{
public static void main(String[] args)
{
   Date d = new Date();
   d.showDate();
}

}