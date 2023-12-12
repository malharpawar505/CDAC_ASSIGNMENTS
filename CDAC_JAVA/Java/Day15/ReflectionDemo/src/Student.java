import java.util.Objects;

public class Student {
    int rollno;
    String name;

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (!(o instanceof Student student)) return false;
        return rollno == student.rollno && Objects.equals(name, student.name);
    }

    @Override
    public int hashCode() {
        return Objects.hash(rollno, name);
    }

    public int getRollno() {
        return rollno;
    }

    public void setRollno(int rollno) {
        this.rollno = rollno;
    }

    public Student() {
    }

    public Student(int rollno, String name) {
        this.rollno = rollno;
        this.name = name;
    }
}
