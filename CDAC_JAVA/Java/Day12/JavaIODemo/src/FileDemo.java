import java.io.*;
import java.nio.charset.StandardCharsets;

public class FileDemo {
    public static void main(String[] args) throws FileNotFoundException, IOException {

       /* FileInputStream fs = new FileInputStream("C:\\Mydata\\mytext.txt");
        int i;
        while((i=fs.read()) != -1)
            System.out.print((char)i);

        fs.close();*/

        /*
        FileReader fs = new FileReader("C:/Mydata/mytext.txt");
        int i;
        while((i=fs.read()) != -1)
            System.out.print((char)i);

        fs.close();

         */
/*
        FileOutputStream fos = new FileOutputStream("C:/Mydata/mytext1.txt",true);
        String s= "  Java module is going on !!";
        fos.write(s.getBytes());
        fos.close(); */

        /*
        FileWriter fos = new FileWriter("C:/Mydata/mytext2.txt",true);
        String s= "  Java module is going on !!";
        fos.write(s);
        fos.close();

         */

        File f = new File("C:/Mydata/mytext2.txt");
        System.out.println(f.isFile());
        System.out.println(f.isDirectory());
        System.out.println(f.canRead());
        System.out.println(f.canWrite());
        System.out.println(f.exists());
        System.out.println(f.length());
        System.out.println(f.getName());
        System.out.println(f.getAbsolutePath());


        FileReader fs = new FileReader(f);
        int i;
        if(f.exists()) {
            while ((i = fs.read()) != -1)
                System.out.print((char) i);
        }
        fs.close();

        boolean b = f.delete();
        if(b)
            System.out.println("File deleted");


    }
}
