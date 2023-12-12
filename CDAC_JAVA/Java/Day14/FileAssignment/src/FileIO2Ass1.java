import java.io.*;

public class FileIO2Ass1 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        System.out.println("Enter file name along with path");
        String filename = br.readLine();

        File f = new File(filename);
        if(f.isDirectory())
        {
            File[] flist=  f.listFiles();
            for (File  ff:flist) {
                System.out.println(ff.getName());

            }
        }
        else if(f.isFile())
        {

            if(f.length() >25)
            {
                System.out.println("Reading using Buffered");
                  BufferedReader br1 = new BufferedReader(new FileReader(f));
                  int i;
                  char[] arr = new char[20];
                  while((i= br1.read(arr)) != -1) {
                      System.out.print(arr);
                  }
                  br1.close();
            }
            else {
                System.out.println("Reading using char by char");
                FileReader fr  = new FileReader(f);
                int i;
                while((i= fr.read()) != -1) {
                    System.out.print((char)i);
                }
                fr.close();
            }

        }
        br.close();
    }
}
