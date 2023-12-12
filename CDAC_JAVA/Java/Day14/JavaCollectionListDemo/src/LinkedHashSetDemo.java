import java.util.*;

public class LinkedHashSetDemo {
    public static void main(String[] args) {
        //1st way Creating arraylist object
        //ArrayList<String> arr = new ArrayList<>();
        //2nd way
        Set<String> arr = new LinkedHashSet<>();


        //Adding diif elements in Arraylist
        arr.add("Radha");
        arr.add("Keshav"); //duplicate data
        arr.add("Vishal");
        arr.add("Sharvari");
        arr.add("Sudha");
        arr.add("Ashok");



        //arr.add(1,"Rama"); //Insert using index will not work for HashSet

        System.out.println(arr);

        //arr.remove(2); //remove by index will not work for HashSet
        arr.remove("Radha"); //remove by value
        arr.remove("Vishal"); //remove by value



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
        // ListIterator<String> itrlst= arr.listIterator(); Not Available in HashSet

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


        System.out.println("Duplicate elements are not allowed.");
        System.out.println("Order of element is maintained.");



    }
}
