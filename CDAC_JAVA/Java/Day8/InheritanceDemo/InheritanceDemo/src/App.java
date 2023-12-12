import office.general.Person;
import office.staff.Emp;

public class App {
    public static void main(String[] args) throws Exception {
        
     //Emp e = new Emp(12,4005.9f);
     //e.name="Radha";

     /* 
     Person p = new Person();
     p.display();

     Emp e = new Emp();
     e.display();
     
     Programmer p1 = new Programmer();
     p1.display();     
     //System.out.println(e);
     */
/* 
    Object o = new Person();
    Object o1 = new Emp();
    Object o2 = new Programmer();

    Person p;//Generic referance or polymorphic variable
     p = new Person();
     p.display();

     p = new Emp();
     p.display();

     p = new Programmer();
     p.display();
*/


     Person p;//Generic referance or polymorphic variable
     

     p = new Emp();
     p.display();

     p = new Programmer();
     p.display();



/* 
 Person p = new Person();
 Person p1 = p.getCurrentObj();  
 System.out.println(p1 instanceof Person);


 Emp e = new Emp();
 Emp e1 = e.getCurrentObj();  
 System.out.println(e1 instanceof Emp);


*/

    }
}
