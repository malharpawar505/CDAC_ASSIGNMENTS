public class Account
{
  private int acno;
  private double balance;
  private static float int_rate=4.5f;

static{
System.out.println("Instatic Block ");
   int_rate= 5.5f;
}

  public Account()
{
  acno = 0;
  balance = 0.0;
}

public Account(int no,double bal)
{
  this.acno = no;
  this.balance = bal;
}

public void calculateIntrest()
{
  double intrest = balance*int_rate/100;
   System.out.println("Intrest of "+acno+"  is "+ intrest);
}

public static void updateIntrest(float rt)
{
  int_rate = rt;
}

public void displayAccount()
{
  System.out.println(this.acno + "--"+this.balance+"--"+ int_rate);
  calculateIntrest();
}

}