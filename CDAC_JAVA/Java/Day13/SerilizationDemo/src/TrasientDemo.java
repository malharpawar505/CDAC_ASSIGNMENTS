import java.io.*;

public class TrasientDemo {
    public static void main(String[] args) throws IOException,ClassNotFoundException {
        PrimaryStudent[] sarr = new PrimaryStudent[3];
        sarr[0] = new PrimaryStudent(12,"Ravi",98.67f);
        sarr[1] = new PrimaryStudent(13,"Kishori",88.67f);
        sarr[2] = new PrimaryStudent(14,"Rama",66.67f);

        for(PrimaryStudent s:sarr)
            System.out.println(s);

        ObjectOutputStream os = new ObjectOutputStream(new FileOutputStream("C:\\Mydata\\myobj.dat"));
        for(PrimaryStudent s:sarr)
            os.writeObject(s);
        os.close();
        System.out.println("Successfully Written all Objects to file");

        ObjectInputStream ois = new ObjectInputStream(new FileInputStream("C:\\Mydata\\myobj.dat"));
        while(true) {
            try {
                Object obj = ois.readObject();
                PrimaryStudent s1 = (PrimaryStudent) obj;
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
