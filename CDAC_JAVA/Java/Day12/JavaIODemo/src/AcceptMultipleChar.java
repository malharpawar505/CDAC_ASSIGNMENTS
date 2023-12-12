import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class AcceptMultipleChar {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int i;
        while((i = br.read()) != 'q')
            System.out.println((char) i);
        br.close();
    }
}
