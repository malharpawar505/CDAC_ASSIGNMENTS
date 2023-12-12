public interface Drawable
{
    void draw();
    default void msg()
    {
        System.out.println("In msg");
    }

    static void statMethod()
    {
        System.out.println("static");
    }
} 