import java.util.ArrayList;
import java.util.List;

public class StoringObjDemo {
    public static void main(String[] args) {
        List<Student> stdList = new ArrayList<>();
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

        Student s1 = new Student(12,"Ravi","Pune",78.90f);
        Student s2= new Student(12,"Ravi","Pune",78.90f);//s1;

        if(s1==s2)
            System.out.println("Both are Same using ==");
        else
            System.out.println("Both are Different == method");


        if(s1.equals(s2))
            System.out.println("Both are Same using equals");
        else
            System.out.println("Both are Different using equals");







    }


}


