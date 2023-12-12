package office.general;
public abstract class Person
{
   //protected String name;
   private String name;
  private long mobile;
public Person() {
   // System.out.println("In Persons Default Constructor");
}
public Person(String name, long mobile) {
    this.name = name;
    this.mobile = mobile;
    //System.out.println("In Persons Parametrised Constructor");
}

/* 
public void display()
{
    System.out.println("In Persons display");
}
*/

public abstract void display();
public Person getCurrentObj()
{
    System.out.println("In Persons getCurrentObj");
    return this;
}


@Override
public String toString() {
    return "Person [name=" + name + ", mobile=" + mobile + "]";
}
 


}