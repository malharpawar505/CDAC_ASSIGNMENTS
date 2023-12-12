import java.lang.reflect.Constructor;
import java.lang.reflect.Method;

public class ReflectionDemo {

        public static void main(String[] args) {
           // String s= "";
            Student s = new Student();
            Class cls = s.getClass();
            System.out.println(cls.getName());

            System.out.println("\n----Constructors-----\n");
            Constructor[] conarr = cls.getConstructors();
            for (Constructor con:conarr) {
                System.out.println(con);

            }

            System.out.println("\n----Methods-----\n");
            Method[] methodsarr = cls.getMethods();
            for (Method m:methodsarr) {
                System.out.println(m);

            }

            System.out.println("----Iterfaces-----");
            Class[] intfac = cls.getInterfaces();
            for (Class con:intfac) {
                System.out.println(con.getName());

            }

            Class sup = cls.getSuperclass();
            System.out.println(sup.getName());

            System.out.println(cls.getPackageName());


        }
    }

