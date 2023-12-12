add<-function(a,b)
{
  a+b
}
add(4,5)
add(7,9)
#--------------------------
add<-function(a,b)
{
  return(a+b)
}
add(4,5)
add(7,9)

#--------------------------
add<-function(a,b)
{
  return(a+b)
}
a=add(4,5)
a
b=add(7,9)
b

#----------------------
#--------------------------
add<-function(a,b)
{
  return(a+b)
}
a=add(4,5)
print(a)
b=add(7,9)
print(b)
#--------------------------
#Default values
add<-function(a,b=5)
{
  return(a+b)
}
a=add(4)
print(a)
b=add(7,9)
print(b)

c= add(b=10,6)
print(c)

#keyword Arguments
d= add(b=20,a=34) 
print(d)

#-------------------------
#infinite
add<-function(a,b,...)
{
  return(a+b+sum(...))
}

add(1,2,3,4,5,6,7,8,9,10)
add(1,2,3,4,5,6)
add(1,2,3,4,5)

#ls is used to print object in memory
ls()
