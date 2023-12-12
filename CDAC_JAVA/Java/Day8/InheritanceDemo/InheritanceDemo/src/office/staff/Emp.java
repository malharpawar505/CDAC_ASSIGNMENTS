package office.staff;
import office.general.Person;
public class Emp extends Person {
    private int empno;
    private float salary ;
    public Emp() {
        //System.out.println("In Emps Default Constructor");
    }

    public Emp(int empno, float salary) {
        super("Snehal", 100);
        //this.name ="hi";
        this.empno = empno;
        this.salary = salary;
      //  System.out.println("In Emps Parametrised Constructor");
    }
//@Override
/* 
    public void display()
{
    System.out.println("In Emp display");
}
*/
  public String toString() {
        return super.toString()+"Emp [empno=" + empno + ", salary=" + salary + "]";
    }

    @Override
    public Emp getCurrentObj()
{
    System.out.println("In Emp getCurrentObj");
    return this;
}
}
