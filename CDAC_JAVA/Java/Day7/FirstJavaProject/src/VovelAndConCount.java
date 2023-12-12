public class VovelAndConCount {
    public static void main(String[] args) {
            String s= "HelloWorld!";
            s= s.toLowerCase();
            char[] arr = s.toCharArray();
            int vcnt=0,ccnt=0;
            for(int i = 0;i<arr.length;i++)
            {
               if(arr[i] >='a' && arr[i]<='z')
               {
                  if(arr[i] =='a' || arr[i] =='e' ||arr[i] =='i' ||arr[i] =='o' ||arr[i] =='u')
                  vcnt ++;
                  else
                  ccnt++;
               }
            
            }
            System.out.println("Consonant Count = "+ccnt);
            System.out.println("Vowels Count = "+vcnt);


    }
}
