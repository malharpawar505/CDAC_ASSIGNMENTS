import java.util.*;
import java.util.Date;
import java.util.Iterator;
import java.util.ListIterator;

public class ArrayListDemo {
    public static void main(String[] args) {
        //1st way Creating arraylist object
        //ArrayList<String> arr = new ArrayList<>();
        //2nd way
        List<String> arr = new ArrayList<>();


        //Adding diif elements in Arraylist
        arr.add("Radha");
        arr.add("Keshav"); //duplicate data
        arr.add("Vishal");
        arr.add("Keshav");
        arr.add("Vishal");

        arr.add(1,"Rama"); //Insert using index

        System.out.println(arr);

        arr.remove(2); //remove by index
        arr.remove("Radha"); //remove by value
        arr.remove("Vishal"); //remove by value only 1st occurance

        //arr.add(23); error
        //arr.add(new Date());//error

        //1st Displaying with sout using tosting
        System.out.println(arr);

        System.out.println("-------------------------------");
       //2nd Displaying with smart for loop
        for (String s:arr ) {
            System.out.println(s);
        }
        System.out.println("-------------------------------");
        //3rd Displaying using Iterable --Iterator method
        Iterator<String> itr= arr.iterator();
        while(itr.hasNext())
        {
            System.out.println(itr.next());
        }


        System.out.println("-----------Print List in Reverse Order--------------------");
        //4th
        ListIterator<String> itrlst= arr.listIterator();
        while (itrlst.hasNext())
            itrlst.next();
        while(itrlst.hasPrevious())
        {
            System.out.println(itrlst.previous());
        }
        System.out.println("-----------end of Print List in Reverse Order--------------------");


        System.out.println("Size of arr: "+arr.size());
        System.out.println("arr is empty? "+arr.isEmpty());

        //Demo of renoveall
        ArrayList<String> arr1 = new ArrayList<>();
        arr1.add("Rama");
        arr1.add("Vishal");
        arr1.add("Vishal1");

        System.out.println("Remove all method demo ------------");
        System.out.println("Orignal arr: "+arr);
        arr.removeAll(arr1);
        System.out.println("after removeall arr :"+arr);
        System.out.println("arr1: "+arr1);

        System.out.println("\n-------------------\n");

        System.out.println("demo of Sorting ------------");
        arr.add("Rama");
        arr.add("Vishal");
        arr.add("Ashok");
        System.out.println("Orignal arr: "+arr);
        Collections.sort(arr);
        System.out.println("after Sorting :");
        System.out.println("arr: "+arr);

        System.out.println("demo of Searching ------------");
        int index = Collections.binarySearch(arr,"Keshav");
        System.out.println("Element found at :"+ index);


        System.out.println("Duplicate elements are allowed.");
        System.out.println("Order of element is maintained.");


    }
}
