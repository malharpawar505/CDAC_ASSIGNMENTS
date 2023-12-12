import java.io.BufferedReader;
import java.io.FileReader;

public class FileIO2Ass4 {
    public static void main(String[] args) throws Exception {
        FileReader fr = new FileReader("C:/Mydata/myfiledata.txt");
        BufferedReader br1 = new BufferedReader(fr);
        String data;
        int maxchar =0;

        while((data= br1.readLine()) != null)
        {
            if(data.length() > maxchar) {
                maxchar = data.length();

            }
        }
        br1.close();

        BufferedReader cm =new BufferedReader(new FileReader("C:/Mydata/myfiledata.txt"));
        while((data=cm.readLine())!=null)
        {
            int l=maxchar-data.length();
            for(int i=0;i<=l;i++)
            {
                System.out.print("-");
            }
            System.out.println(data);

        }
        cm.close();


    }
}
