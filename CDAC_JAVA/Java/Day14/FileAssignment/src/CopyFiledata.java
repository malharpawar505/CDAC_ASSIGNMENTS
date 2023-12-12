import java.io.*;

public class CopyFiledata {
    public static void main(String[] args) throws IOException {
//To Accept Source and Dest from User
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String source = br.readLine();
        String dest = br.readLine();


        String data;
        FileReader fr = new FileReader("C:/MyData/"+source);
        BufferedReader br1 = new BufferedReader(fr);
        //"C:/MyData/myfile.txt"
        FileWriter fw = new FileWriter("C:/MyData/"+dest);

        while((data= br1.readLine()) != null)
        {
            fw.write(data+"\n");
        }
        br.close();
        br1.close();
        fw.close();
        System.out.println("FileWriting Completed");
    }
}
