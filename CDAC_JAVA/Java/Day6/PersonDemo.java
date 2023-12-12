public class PersonDemo
{
  public static void main(String[] args)
{
 Person p = new Person();
System.out.println("--------------------------------");
System.out.println("Only p "+ p);
System.out.println(" p.toString(): "+p.toString());
String s = p.toString();
p.display(p.toString());

}
}