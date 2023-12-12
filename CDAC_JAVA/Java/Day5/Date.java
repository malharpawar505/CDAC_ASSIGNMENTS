class Date{

private int dd,mm,yy;

//No Argument Constructor
public Date()
{
/*
  dd=2;
  mm= 4;
 yy= 1945;*/
this(2,4,1945);
System.out.println("No Argument Constructor");
}

//Parametrise Constructor
//public Date(int d,int m,int y)
public Date(int dd,int mm,int yy)
{
  this.dd=dd;
  this.mm= mm;
  this.yy= yy;
System.out.println("Parametrised Constructor");

}


//Copy Constructor
public Date(Date dt)
{
  dd=dt.dd;
  mm= dt.mm;
 yy= dt.yy;
}


public void showDate()
{
  System.out.println(dd +"-"+mm+"-"+yy);
}

public void showDate(char ch)
{
  System.out.println(dd +" "+ch+mm+" "+ch+yy);
}


}