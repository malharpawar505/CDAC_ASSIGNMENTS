package office.utility.myclasses;
public class Date{

private int dd,mm,yy;

//No Argument Constructor
public Date()
{
  dd=2;
  mm= 4;
 yy= 1945;

}

public int getYy()
{
 return this.yy;
}


public void setYy(int yy)
{
  this.yy= yy;
}


public int getMm()
{
 return this.mm;
}


public void setMm(int mm)
{
  this.mm= mm;
}

public int getDd()
{
 return this.dd;
}


public void Dd(int dd)
{
  this.dd= dd;
}

public Date(int dd,int mm,int yy)
{
  this.dd=dd;
  this.mm= mm;
  this.yy= yy;


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


public String toString()
{
   return dd +"-"+mm+"-"+yy;
}

}