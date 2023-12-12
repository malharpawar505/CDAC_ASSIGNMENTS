import java.util.PriorityQueue;
import java.util.Queue;

public class PriorityQueueDemo {
    public static void main(String[] args) {
        Queue<String> que = new PriorityQueue<>();
        que.add("Snehal");
        que.add("Ravi");
        que.add("Ashok");
        que.add("Sudha");
        que.add("Arnav");
        que.add("Avani");
        que.add("Mayuresh");
        que.add("Babita");
        que.add("Keshav");


        for (String s:que
             ) {
            System.out.println(s);

        }
        System.out.println("-------------------");
        while(!que.isEmpty())
            System.out.println(que.poll());



    }

}
