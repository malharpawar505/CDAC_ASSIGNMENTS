public class RollComparer implements Comparer {

    @Override
    public int compare(Object o1, Object o2) {
        Student s1 = (Student)o1;
        Student s2 = (Student)o2;
        return  s1.getRollno()-s2.getRollno();

    
    }
    
}
