import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class AcceptStringData {
    public static void main(String[] args) throws IOException {
        BufferedReader br  = new BufferedReader(new InputStreamReader(System.in));
        /*
        String s = br.readLine();
        System.out.println(s);
        */
        String s;
        while(!(s=br.readLine()).equals("stop"))
            //System.out.println(s);
            System.err.println(s);


        br.close();
    }
}
