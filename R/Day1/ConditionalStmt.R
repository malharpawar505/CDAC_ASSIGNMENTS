a<-12
if(a>0)
{
  print("A is positive")
}
#----------------------
a<--12
if(a>0)
{
  print("A is positive")
}else{
  print("A is -ve")
}
#-----------------------
a<- 12
b<- 34
c<- 20
if(a> b )
{
  if(a>c)
    print("a is bigger")
  else
    print("c is big")
}else if(b>c)
{
  print("b is bigger")
}else{
  print("c is bigger")
}

#-----------------------
a<- 12
b<- 34
choice<- readline("Enter Choice")

switch(choice,
      "add" = cat(a+b),
      "sub" = cat(a-b),
      "div" = cat(a/b),
      "pow" = cat(a^b),
      print("Invalid choice")
      )
#-------------------------------
no<-2
x<-switch(no,
          "One","Two","Three")
print(x)






