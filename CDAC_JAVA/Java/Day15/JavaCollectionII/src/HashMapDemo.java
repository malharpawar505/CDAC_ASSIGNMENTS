import java.util.HashMap;
import java.util.*;

public class HashMapDemo {
    public static void main(String[] args) {
        Map<Integer,String> hashmap = new HashMap<>();
        hashmap.put(1,"Sachin");
        hashmap.put(34,"Raman");
        hashmap.put(11,"Shrinath");
        hashmap.put(14,"Sachin");
        hashmap.put(8,"Vinod");
        hashmap.put(41,"Nayan");
        hashmap.put(8,"Vikas");

        Set<Integer> keys = hashmap.keySet();
        for (Integer k: keys ) {
            System.out.println(k + " : "+hashmap.get(k));
        }

        System.out.println("Order of Insertion is not maintained");
        System.out.println("Duplicate Keys are override");
        System.out.println("Duplicate Values are allowed");


    }
}
