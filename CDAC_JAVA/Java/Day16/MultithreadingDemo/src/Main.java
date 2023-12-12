public class Main {
    public static void main(String[] args) {

        Thread t = Thread.currentThread(); //Current thread
        System.out.println(t.getName());
        System.out.println(t.getPriority());
        t.setName("My Thread Demo"); //Setting Name
        t.setPriority(10);
        System.out.println("MAX_PRIORITY : " +Thread.MAX_PRIORITY);
        System.out.println("MIN_PRIORITY : "+ Thread.MIN_PRIORITY);
        System.out.println("NORM_PRIORITY : " +Thread.NORM_PRIORITY);

        System.out.println("Values After Modification: ");
        System.out.println(t.getName());
        System.out.println(t.getPriority());

    }
}