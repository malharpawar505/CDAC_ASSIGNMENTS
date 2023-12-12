public class Person
{

private String name;
private Date bDate;

public Person()
{
 name="XYZ";
 bDate= new Date(1,1,2001);
}

public Person(String s,int dd, int mm, int yy)
{
 name=s;
 bDate= new Date(dd,mm,yy);
}

public Person(String s,Date dt)
{
 name=s;
 bDate= dt;
}


public Person(Person p)
{
 name=p.name;
 bDate= p.bDate;
}

public void displayPerson()
{
  System.out.println(name);
System.out.println(bDate);
if(bDate != null)
bDate.showDate();

}
}