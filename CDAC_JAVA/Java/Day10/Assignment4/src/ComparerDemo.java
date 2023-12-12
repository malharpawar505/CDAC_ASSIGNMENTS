import java.util.Scanner;

public class ComparerDemo {
    public static void main(String[] args) {
        Student[] sarr = new Student[3];
        sarr[0] = new Student(12,"Geeta",78.56f);
        sarr[1] = new Student(6,"Ashwini",88.56f);
        sarr[2] = new Student(3,"Renuka",98.56f);
    
         for (Student student : sarr) {
            System.out.println(student);
         }
    
         Scanner sc = new Scanner(System.in);
         System.out.println("Enter Your Choice for sorting \n 1. Rollno 2.Name 3.Marks");
         int choice = sc.nextInt();
         Comparer cobj = null;
         switch (choice) {
            case 1:
                cobj = new RollComparer();
                break;
           case 2:
                cobj = new NameComparer();
                break;
            case 3:
                cobj = new MeritComparer();
                break;
            default:
            System.out.println("Enter Valid Choice");
                break;
         }

         for (int index = 0; index < sarr.length; index++) {
            for (int j = index+1; j < sarr.length; j++) {
                if(cobj.compare(sarr[index], sarr[j]) >0 )
                {
                    Student temp = sarr[index];
                    sarr[index] = sarr[j];
                    sarr[j]= temp;

                }//if
            
         }//for

         //
         
         }//for
System.out.println("Array element after Sorting:\n");
         for (Student student : sarr) {
            System.out.println(student);
            
         }
    
    }
    
}
