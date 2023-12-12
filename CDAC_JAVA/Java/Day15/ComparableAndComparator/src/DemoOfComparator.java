                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       import java.util.Comparator;
import java.util.*;

public class DemoOfComparator {
    public static void main(String[] args) {
       Set<Emp>  emplist = new TreeSet<>(
               new Comparator<Object>() {

           @Override
           public int compare(Object o1, Object o2) {
               Emp e = (Emp)o1;
               Emp e1 = (Emp)o2;
               //return  e.getEmpid()-e1.getEmpid(); //soring by empid
               return  e.getEname().compareTo(e1.getEname()); //soring by ename

           }
       });

        emplist.add(new Emp(12,"Sudha",21312.56f,"Pune"));
        emplist.add(new Emp(11,"Ashok",80000,"Pune"));
        emplist.add(new Emp(22,"Arnav",4567,"Nashik"));
        emplist.add(new Emp(35,"Vinod",1312.56f,"Nagar"));
        emplist.add(new Emp(52,"Nayan",221312.56f,"Nashik"));
        emplist.add(new Emp(2,"Rama",212.56f,"Pune"));

        for (Emp e: emplist) {
            System.out.println(e);
        }
        }
        }
    


