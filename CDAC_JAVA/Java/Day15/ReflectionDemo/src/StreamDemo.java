import java.util.Arrays;
import java.util.stream.IntStream;

public class StreamDemo {
    public static void main(String[] args) {
        IntStream is = IntStream.of(1,2,3,4,5,6);
        is.forEach(System.out::println);
        System.out.println("-----------------------------");

        int[] arr={12,3,4,5,6,7};
        IntStream iss = Arrays.stream(arr);
        iss.forEach(System.out::println);

        System.out.println("-----------------------------");

        IntStream is1 = IntStream.range(1,12); //Generate no 1 to 11
        is1.forEach(System.out::println);
        System.out.println("-----------------------------");

        IntStream is3 = IntStream.rangeClosed(1,12); //Generate no 1 to 12
        is3.forEach(System.out::println);
        System.out.println("-----------------------------");

        System.out.println("------------Mathamatical-----------------");
        IntStream is2 = IntStream.rangeClosed(1,12);
        int max = is2.max().getAsInt();
        IntStream is4 = IntStream.rangeClosed(1,20);
        int min = is4.min().getAsInt();

        IntStream is5 = IntStream.rangeClosed(1,12);
        int sum = is5.sum();

        IntStream is6 = IntStream.rangeClosed(1,12);
        double avg = is6.average().getAsDouble() ;

        System.out.println(max);
        System.out.println(min);
        System.out.println(sum);
        System.out.println(avg);



    }
}
