import java.io.*;

public class PersonDemo {

    public static void main(String[] args) throws IOException,ClassNotFoundException {
       /* Person p = new Person("Ravi",2,6,23);

        ObjectOutputStream os = new ObjectOutputStream(new FileOutputStream("C:\\Mydata\\person.dat"));
        os.writeObject(p);
        os.close();
        System.out.println("Successfully Written Obj to file");

        ObjectInputStream ois = new ObjectInputStream(new FileInputStream("C:\\Mydata\\person.dat"));
        Object obj = ois.readObject();
        ois.close();
        Person p1=(Person) obj;
        System.out.println(p1);
        */
        Emp e = new Emp("Ravi",2,6,23,89,6789.90);

        ObjectOutputStream os = new ObjectOutputStream(new FileOutputStream("C:\\Mydata\\person1.dat"));
        os.writeObject(e);
        os.close();
        System.out.println("Successfully Written Obj to file");

        ObjectInputStream ois = new ObjectInputStream(new FileInputStream("C:\\Mydata\\person1.dat"));
        Object obj = ois.readObject();
        ois.close();
        Emp e1=(Emp) obj;
        System.out.println(e1);

    }
}
