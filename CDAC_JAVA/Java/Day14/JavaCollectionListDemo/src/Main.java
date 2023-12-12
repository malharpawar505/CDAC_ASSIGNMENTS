import java.util.ArrayList;

// Press Shift twice to open the Search Everywhere dialog and type `show whitespaces`,
// then press Enter. You can now see whitespace characters in your code.
public class Main {
    public static void main(String[] args) {
        ArrayList arrlst = new ArrayList(20);
        arrlst.add("Geeta");
        arrlst.add("Radha");
        arrlst.add(10);
        arrlst.add(10.78f);
        arrlst.add(new Date());
        System.out.println(arrlst);
        arrlst.add(2,700);

        System.out.println("----------------------------------");
        System.out.println(arrlst);

        System.out.println("----------------------------------");
        for (Object o:arrlst) {
            System.out.println(o);
        }

        System.out.println("----------------------------------");
        for (Object o:arrlst) {
            if(o instanceof String)
            System.out.println(((String) o).toUpperCase());
        }





    }
}