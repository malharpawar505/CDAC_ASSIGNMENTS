public class DateDemo
{
  public static void main(String[] args)
{
 Date d = new Date();
d.showDate();
d.setYy(2023);
d.showDate();
System.out.println(d.getYy());
d.setMm(12);
System.out.println(d.getMm());
d.showDate();
System.out.println("--------------------------------");
System.out.println("Only d "+ d);
System.out.println(" d.toString(): "+d.toString());

}
}