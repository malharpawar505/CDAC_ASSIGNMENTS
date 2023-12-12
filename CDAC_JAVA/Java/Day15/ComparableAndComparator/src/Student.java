import java.security.cert.TrustAnchor;

//implemented Comparable for SOrting Student data in TreeSet
public class Student implements Comparable<Student> {
    private  int rollno;
    private String name;
    private String city;
    private float per;

    public Student() {
    }

    @Override
    public String toString() {
        return "Student{" +
                "rollno=" + rollno +
                ", name='" + name + '\'' +
                ", city='" + city + '\'' +
                ", per=" + per +
                '}';
    }

    public Student(int rollno, String name, String city, float per) {
        this.rollno = rollno;
        this.name = name;
        this.city = city;
        this.per = per;
    }

    @Override
    public int hashCode() {
        if(city.equals("Pune"))
            return 10;
        else if(city.equals("Nashik"))
            return 20;
        else if(city.equals("Nagar"))
            return 30;
        else
            return 40;



        /*
        if(rollno >=1 && rollno <=30)
            return 10;
        else if(rollno >=31 && rollno <=60)
            return 20;
        else if(rollno >=61 && rollno <=100)
            return 30;
        else
            return 40;*/
    }

    public int getRollno() {
        return  rollno;

    }

    public void setRollno(int rollno) {
        this.rollno = rollno;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getCity() {
        return city;
    }

    public void setCity(String city) {
        this.city = city;
    }

    public float getPer() {
        return per;
    }

    public void setPer(float per) {
        this.per = per;
    }

    @Override
    public boolean equals(Object obj) {
        Student s= (Student)obj;
        if(this.rollno == s.rollno && this.name.equals(s.name) && this.city.equals(s.city) && this.per == s.per)
            return true;
        else
            return false;

    }

    @Override
    public int compareTo(Student o) {
        //Comparing data using rollno
       // return this.rollno -o.rollno;

        //Comparison Using Descending Order
        //return o.rollno-this.rollno;

        //Comparing data using name
        //return this.name.compareTo(o.name);

        /*
        //Per comaprison using descending order
        if(o.per -this.per>0)
            return 1;
        else if(o.per -this.per<0)
            return -1;
        else
            return 0;

         */

        //Comparing data using City

        if(this.city.compareTo(o.city) == 0)
            return this.rollno - o.rollno;
        else
           return this.city.compareTo(o.city);


    }
}
