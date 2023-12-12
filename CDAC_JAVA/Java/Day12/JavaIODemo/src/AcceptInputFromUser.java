import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class AcceptInputFromUser {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int id = Integer.parseInt(br.readLine());
        double d = Double.parseDouble(br.readLine());
        float f = Float.parseFloat(br.readLine());
        String s = br.readLine();
        char c = (char)br.read();

        System.out.println(id);
        System.out.println(d);
        System.out.println(f);
        System.out.println(s);
        System.out.println(c);


    }
}
