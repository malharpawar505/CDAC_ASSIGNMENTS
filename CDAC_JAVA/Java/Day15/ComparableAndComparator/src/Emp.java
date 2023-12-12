public class Emp {
    private int empid;
    private String ename;
    private float salary;
    private String city;

    @Override
    public String toString() {
        return "Emp{" +
                "empid=" + empid +
                ", ename='" + ename + '\'' +
                ", salary=" + salary +
                ", city='" + city + '\'' +
                '}';
    }

    public Emp(int empid, String ename, float salary, String city) {
        this.empid = empid;
        this.ename = ename;
        this.salary = salary;
        this.city = city;
    }

    public Emp() {
    }

    public int getEmpid() {
        return empid;
    }

    public void setEmpid(int empid) {
        this.empid = empid;
    }

    public String getEname() {
        return ename;
    }

    public void setEname(String ename) {
        this.ename = ename;
    }

    public float getSalary() {
        return salary;
    }

    public void setSalary(float salary) {
        this.salary = salary;
    }

    public String getCity() {
        return city;
    }

    public void setCity(String city) {
        this.city = city;
    }
}
