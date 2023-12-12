import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException,ClassNotFoundException {

       /* Student s = new Student(12,"Ravi",98.67f);

        ObjectOutputStream os = new ObjectOutputStream(new FileOutputStream("C:\\Mydata\\myobj.dat"));
        os.writeObject(s);
        os.close();
        System.out.println("Successfully Written Obj to file");

        ObjectInputStream ois = new ObjectInputStream(new FileInputStream("C:\\Mydata\\myobj.dat"));
        Object obj = ois.readObject();
        ois.close();
        Student s1=(Student)obj;
        System.out.println(s1);

        */

        Student[] sarr = new Student[3];
        sarr[0] = new Student(12,"Ravi",98.67f);
        sarr[1] = new Student(13,"Kishori",88.67f);
        sarr[2] = new Student(14,"Rama",66.67f);

        ObjectOutputStream os = new ObjectOutputStream(new FileOutputStream("C:\\Mydata\\myobj.dat"));
       for(Student s:sarr)
            os.writeObject(s);
        os.close();
        System.out.println("Successfully Written all Objects to file");

        ObjectInputStream ois = new ObjectInputStream(new FileInputStream("C:\\Mydata\\myobj.dat"));
        while(true) {
            try {
                Object obj = ois.readObject();
                Student s1 = (Student) obj;
                System.out.println(s1);
            }
            catch (Exception e)
            {
                System.out.println(e.toString());
                break;
            }
        }

        ois.close();



    }
}