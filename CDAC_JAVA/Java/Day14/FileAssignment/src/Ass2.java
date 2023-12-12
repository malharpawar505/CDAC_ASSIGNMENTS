import java.io.*;
import java.sql.SQLOutput;
import java.util.SortedMap;

public class Ass2 {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String fname = br.readLine();
        String data;
        int maxchar=0;
        String smax="";

        FileWriter fw = new FileWriter("C:/MyData/"+fname);
        System.out.println("Enter data for file");
        while(!(data = br.readLine()).equals("quit"))
            fw.write(data+"\n");
        fw.close();


        FileReader fr = new FileReader("C:/MyData/"+fname);
        BufferedReader br1 = new BufferedReader(fr);
        //"C:/MyData/myfile.txt"
        while((data= br1.readLine()) != null)
        {
            if(data.length() > maxchar) {
                maxchar = data.length();
                smax= data;
            }
            System.out.println(data);
        }
        br.close();

        br1.close();

        System.out.println("-----------------------");
        System.out.println(maxchar);
        System.out.println(smax);


    }
}
