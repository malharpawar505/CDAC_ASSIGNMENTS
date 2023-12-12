#Vector Creation
v<- c(1,2,3,4,5)
v

v<-1:10
v

v<-c(1,2,3,4.5)
v

v<-c("a","b","c","d")
v

v<- c(1,2,3,4,5,"a")
v

v<-seq(1,10,by=2)
v

v<-seq(1,5,by=0.5)
v

v<-seq(1,5)#default val is 1
v

v<-rep(10,each=3)
v

v<-rep(1:3,each=3)
v

v<-rep(1:3,times=3)
v

v<-rep(1:3,times=3,each=2)
v

v<-rep(1:3,each=2,times=3)
v
class(v)
typeof(v)

#Mathematical Operation on Single Vector

v<- c(1,2,3,4,5)
v

v+1

v*2

v^3

v%%2

#Mathematical Operation on Two Vector
#Must have vectors of same length to perform all mathamatical operations
v<- c(1,2,3,4,5)
v

v1<-c(10,20,30,40,50)
v1

v+v1

v1-v

v1*v

#----------
v<- c(1,2,3,4,5)
v

v1<-c(10,20,30,40,50,60)
v1

v+v1 #error as v1 having more values

#----------Functions--------------------
v<- c(61,2,33,14,5,2,33)
v

sort(v) #by default ascending

sort(v,decreasing = TRUE) #descending 

unique(v)

v
rev(v) #reverse vector

table(v) #no of times given ele present in vector


v
sum(v)
length(v)
min(v)
max(v)
mean(v)
median(v)
sd(v)
var(v)
summary(v)
str(v)
#-------------------------------------
#Accessing the Vector Element
v<-11:20
v
v[4]

v[1:3]

v[c(3,6,8)]


v[-4]

v[-1:-3]

v[-c(3,6,8)]

v[c(-3,-6,-8)]

v[v==15]


v[v>=15]

v[v%%2==0]

v[v%%2==1]


v[v>=13 & v<=17]


v[v %in% c(12,14,19)]


v<- c("a"=10,"b"=20,"c"=30)
v

v["a"]

names(v) #return you all names of element

#-------------------------------------
v<-c(1,2,NA,3,4,5)
v
sum(v)
min(v)
max(v)
#---------
sum(v,na.rm =T)
min(v,na.rm =T)
max(v,na.rm =T)

#--------------------

v<-c(1,2,12,13,14,3,4,5)
v
ifelse(v%%2==0,"even","odd")






