public class Person
{
   private String name;
  private long mobile;
public Person() {
    System.out.println("In Persons Default Constructor");
}
public Person(String name, long mobile) {
    this.name = name;
    this.mobile = mobile;
    System.out.println("In Persons Parametrised Constructor");
}



@Override
public String toString() {
    return "Person [name=" + name + ", mobile=" + mobile + "]";
}
 


}