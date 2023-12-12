import java.io.Serializable;

public class Person implements Serializable{
    String name;
    Date dd;

    public Person() {
    }

    public Person(String name, Date dd) {
        this.name = name;
        this.dd = dd;
    }

    public Person(String name, int d,int m,int y) {
        this.name = name;
        this.dd = new Date(d,m,y);
    }

    @Override
    public String toString() {
        return "Person{" +
                "name='" + name + '\'' +
                ", dd=" + dd +
                '}';
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
}

class Date implements  Serializable{
    int dd,mm,yy;

    public Date(int dd, int mm, int yy) {
        this.dd = dd;
        this.mm = mm;
        this.yy = yy;
    }

    public int getDd() {
        return dd;
    }



    public void setDd(int dd) {
        this.dd = dd;
    }

    public int getMm() {
        return mm;
    }

    public void setMm(int mm) {
        this.mm = mm;
    }

    public int getYy() {
        return yy;
    }

    public void setYy(int yy) {
        this.yy = yy;
    }

    @Override
    public String toString() {
        return "Date{" +
                "dd=" + dd +
                ", mm=" + mm +
                ", yy=" + yy +
                '}';
    }
}

class Emp extends Person {
    int empid;
    double salary;


    public Emp(String name, int d, int m, int y, int empid, double salary) {
        super(name, d, m, y);
        this.empid = empid;
        this.salary = salary;
    }

    public int getEmpid() {
        return empid;
    }

    public void setEmpid(int empid) {
        this.empid = empid;
    }

    public double getSalary() {
        return salary;
    }

    public void setSalary(double salary) {
        this.salary = salary;
    }

    @Override
    public String toString() {
        return super.toString() +
                "empid=" + empid +
                ", salary=" + salary +

                '}';
    }
}
