a<-array(dim=c(2,2))
a

a<-array(1:10, dim=c(5,2))
a


a<-array(seq(1,20,by=1),dim=c(2,5,2))
a


a<-array(1:15,dim=c(2,5,2))
a

summary(a)
length(a)
str(a)
sum(a)

#subsetting 
a<-array(10,dim=c(5))
a
a[2]

a<-array(c(12,34,56,78,3),dim=c(5))
a
a[4]

a[-4]

a<-array(1:10,dim=c(2,5))
a

a[1,]
a[,5]
a[,5,drop=F]

a<-array(1:20,dim=c(2,5,2))
a
a[2,5,1] #10

a[2,3,] #return 2nd row 3rd col from both arrays

a[2,,]
