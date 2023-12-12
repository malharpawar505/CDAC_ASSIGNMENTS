import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        try {
            int i = br.read();
            System.out.println( (char)i);
        } catch (IOException e) {
            System.out.println("Error "+e.getMessage());
        }
        finally {
            try {
                br.close();
            } catch (IOException e) {
                System.out.println("Error "+e.getMessage());
            }
        }


    }
}