#creation

m<-matrix(10,3,4)
m


m<-matrix(c(1,2,3,4,5,6,7,8),2,4)
m


m<-matrix(c(1,2,3,4,5,6,7,8),4,2)
m


m<-matrix(c(1,2,3,4,5,6,7,8),4,2,byrow = TRUE)
m

m<-matrix(c(1,2,3,4,5,6,7,8),4,2,byrow = FALSE)
m

m<-matrix(1:20,5,4,byrow = TRUE)
m

#---------------rbind and cbind

x<-1:5
y<-11:15
z<-21:25

m<-rbind(x,y,z)
m

m<-cbind(x,y,z)
m

#----------------Accing Element

m<-matrix(1:20,5,4,byrow = TRUE)
m

m[1,1]
m[2,2]
m[3,] #return entire 3rd row
m[1:3,] #return 1st 3 rows
m[1,1:3] #return 1st row and 1, 2 , 3 cols
m
m[-1,1:3] #exclude 1st row and include 1,2,3 columns
m[-1,-1:-3] #exclude 1st row and exclude 1,2,3 columns
m[-1,-1:-3,drop=F] #exclude 1st row and exclude 1,2,3 columns and display output in vertical way
m
m[c(1,4),c(2,3)] #include 1 and 4th row and 2nd and 3rd columns

m[c(1,4),-c(2,3)]#include 1 and 4th row and exclude 2nd and 3rd columns
m
m[-c(1,4),-c(2,3)]#exclude 1 and 4th row and exclude 2nd and 3rd columns
#-------------------------
m<-matrix(1:4,2,2)
m1<-matrix(11:14,2,2)

m%*%m1 #matrix Multiplication

#-------------------------
length(m)
summary(m)
min(m)
max(m)
sum(m)

