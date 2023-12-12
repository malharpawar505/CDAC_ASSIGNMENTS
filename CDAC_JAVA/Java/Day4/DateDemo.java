
import java.util.Scanner;
class DateDemo{

public static void main(String[] args)
{
  // Date d;
   //d = new Date(11,4,1990);
//	d.showDate();


//Date d1 = new Date(12,4,2023);
	//d1.showDate();


Date d2 = new Date();
	d2.showDate();
d2.showDate('/');
d2.showDate('#');
d2.showDate('.');


//Date d4 = new Date(d); //State of d will be copied to d4
//d4.showDate();

Date[] dtary= new Date[4];
 dtary[0] = new Date(1,3,2013);
dtary[1] = new Date(11,2,2003);
dtary[2] = new Date(7,4,2014);
dtary[3] = new Date();

for(int i = 0;i< dtary.length;i++)
{
    dtary[i].showDate('/');
}


for(Date d:dtary)
	d.showDate();

Scanner sc = new Scanner(System.in);
System.out.println("Enter value for dd,mm,yy");
int d = sc.nextInt();
int m = sc.nextInt();
int y = sc.nextInt();

Date d5 = new Date(d,m,y);
d5.showDate();

 



}

}