public class Emp extends Person {
    private int empno;
    private float salary ;
    public Emp() {
        System.out.println("In Emps Default Constructor");
    }

    public Emp(int empno, float salary) {
        super("Snehal", 100);
        this.empno = empno;
        this.salary = salary;
        System.out.println("In Emps Parametrised Constructor");
    }

  public String toString() {
        return super.toString()+"Emp [empno=" + empno + ", salary=" + salary + "]";
    }

    
}
