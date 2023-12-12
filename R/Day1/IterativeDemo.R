a<-5
while(a>0)
{
  print(a)
  a <- a-1
}
#----------------------------
a<-5
no=1
while(no<=10)
{
  print(a*no)
  no <- no+1
}
#--------------------
# horizontal table of 5 to 12
a<-5
while(a<=12)
{
  no=1
  while(no<=10)
  {
    cat(a*no," ")
    no <- no+1
  }
  a<-a+1
  print("")
}

#--------------------


for (a in 1:10)
{
  print(a)
}
#------------------------
#Print all small case letters from a to z 
for( a in letters)
{
  print(a)
}
#-------------------------
#Print all Upper case letters from A to Z 
for( a in LETTERS)
{
  print(a)
}

#-------------------------
for( a in LETTERS[1:10])
{
  print(a)
}


#-------------------------
for( a in LETTERS[10:20])
{
  print(a)
}

#-------------------------------
#break
a=1
while(a< 10)
{
  if(a==5)
    break
  print(a)
  a<-a+1
}



#------------------
#next
a=0
while(a< 10)
{
  a<-a+1
  if(a==5)
    next
  print(a)
  
}

#------------------
#Repeat

#infinite
repeat{
  print("Hello")
}
#-------------------
cnt<-0
repeat{
  cnt<-cnt+1
  if (cnt == 10)
    break
  print("Hello")
}


#-------------------
no<-0
repeat{
  no <- no+1
  if(no ==30)
    break
  if(no%%3 == 0)
    next
  print(no)
}


