l<- list(1,2,3,4,5)
l

l<-list(1,23L,c(10,20,30),"Mayank","Revati",TRUE,FALSE,23.5)
l
str(l)

l2<-list(a="sudha",b=c(10,20,30))
l2
#------------------Functions
str(l2)
names(l2)

l<- list(1,2,3,4,5)
l
class(l)
typeof(l)
v<-unlist(l) #convert into vector
v
class(v)
typeof(v)

#---------------------Accessing Element
l<- list(1,2,3,4,5)
l
l[1]
l[1:3]
l[-1]
l[-1:-3]
l[c(1,3)]
l[-c(1,3)]
l[l>3]

l<-list(1,23L,c(10,20,30),"Mayank","Revati",TRUE,FALSE,23.5)
l
l[3]
l[[3]][2]
l[4]
l[[4]]



l2<-list(a="sudha",b=c(10,20,30))
l2
l2$a

l2$b
l2$b[2]

summary(l2)

length(l2)
