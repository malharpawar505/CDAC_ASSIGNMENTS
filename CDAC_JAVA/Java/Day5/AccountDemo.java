import static java.lang.System.*;
public class AccountDemo
{
  public static void main(String[] args)
{

Account onlyref;
out.println("Objects are not initialised yet");
	Account a = new Account();
	a.displayAccount();
//Account.int_rate = 12.7f;

Account b = new Account(12,78000);
	b.displayAccount();


Account b1 = new Account(112,8000);
	b1.displayAccount();

out.println("Updating Int rate");
Account.updateIntrest(12.5f);

Account b2 = new Account(121,78000);
	b2.displayAccount();


Account b3 = new Account(127,8000);
	b3.displayAccount();


}

}