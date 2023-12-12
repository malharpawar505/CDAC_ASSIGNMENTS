public class PersonDemo
{
  public static void main(String[] args)
{
/*
   Person p = new Person();
   p.displayPerson();

Person p1 = new Person("PQR",2,2,2002);
   p1.displayPerson();

Date dt = new Date(3,3,2003);
Person p2 = new Person("LMNO",dt);
   p2.displayPerson();

*/

//referance Equality
  Person p = new Person();
   p.displayPerson();
System.out.println("----------------------------");

 Person p1=p;
p1.displayPerson();
if(p== p1)
 System.out.println("Same");
else
 System.out.println("Different");

System.out.println("----------------------------");

Person p2=new Person(p);
p2.displayPerson();
if(p2== p1)
 System.out.println("Same");
else
 System.out.println("Different");

System.out.println("----------------------------");

System.out.println(p instanceof Person);
//System.out.println(p instanceof PersonDemo);
Person p4;
System.out.println(p4 instanceof Person);


}
}
