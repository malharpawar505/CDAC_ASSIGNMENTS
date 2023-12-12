import java.util.HashSet;
import java.util.*;

public class DemoOfTreeSetForComparable {

    public static void main(String[] args) {
        Set<Student> stdList = new TreeSet<>();
        Student s = new Student(12,"Ravi","Pune",78.90f);
        stdList.add(s);
        stdList.add(new Student(13,"Kishori","Nashik",88.90f));
        stdList.add(new Student(1,"Arati","Pune",58.90f));
        stdList.add(new Student(3,"Vashnavi","Nagar",68.90f));
        stdList.add(new Student(14,"Trupti","Goa",81.90f));
        stdList.add(new Student(36,"Deepali","Nashik",85.90f));

        for (Student s1:stdList) {
            System.out.println(s1);
        }

        Boolean res = stdList.contains(new Student(13,"Kishori","Nashik",88.90f));
        System.out.println(res);

        Boolean res1 = stdList.contains(s);
        System.out.println(res1);
        System.out.println("--------------------------");

    }
}
