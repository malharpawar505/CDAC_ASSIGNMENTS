import java.io.Serializable;

public class PrimaryStudent implements Serializable {
    private int rollno;
    private String name;
    private float per;

    private transient char grade;

    public char getGrade() {
        return grade;
    }

    public void setGrade(char grade) {
        this.grade = grade;
    }

    public PrimaryStudent(int rollno, String name, float per) {
        this.rollno = rollno;
        this.name = name;
        this.per = per;
        if(this.per >90)
            grade ='A';
        else if(this.per >80)
            grade ='B';
        else
            grade ='C';
    }

    public PrimaryStudent() {
    }

    @Override
    public String toString() {
        return "Student{" +
                "rollno=" + rollno +
                ", name='" + name + '\'' +
                ", per=" + per +
                ", grade=" + grade +
                '}';
    }

    public int getRollno() {
        return rollno;
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

    public float getPer() {
        return per;
    }

    public void setPer(float per) {
        this.per = per;
    }
}
