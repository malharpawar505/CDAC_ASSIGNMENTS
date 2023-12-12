public class StringDemo {
    public static void main(String[] args) {
    String s= " Welcome ";
    String s1= " welcome ";

    System.out.println( s);
    System.out.println(s.length());
    System.out.println(s.charAt(2));
    System.out.println(s.indexOf("e", 0));
    System.out.println(s.lastIndexOf("e"));
    System.out.println(s.substring(3));
    System.out.println(s.substring(3,6)  );
    System.out.println(s.toUpperCase());
    System.out.println(s.toLowerCase());
    System.out.println(s.trim());
    System.out.println(s.contains("lc"));
    System.out.println(s.equals(s1) );
     System.out.println(s.equalsIgnoreCase(s1) );
     System.out.println(s.compareTo(s1) );
     System.out.println(s.compareToIgnoreCase(s1) );
     System.out.println(s.replace("e","k"));
     System.out.println(s.concat("World"));

     char[] arr = s.toCharArray();
     for (char char1 : arr) {
        System.out.println(char1);
     }



   


    }
}
