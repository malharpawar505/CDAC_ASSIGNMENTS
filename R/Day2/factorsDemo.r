v<- c("Yes","No","Yes","Yes")
v
f<-factor(v)
print(f)

#-----------------------------
v<- c("Male","Female","Male","Male")
v
f<-factor(v,levels = c("Male","Female","TransG"))
print(f)
#-----------------------------

v<-c("Male","Female","Male","Female","Male","Male")
v

f<-factor(v)
f
summary(f)
length(f)

f1<-factor(v,levels=c("Male","Female","TransG"))
f1
summary(f1)

levels(f1)#get levels

levels(f1)<-c("M","F","T")#set levels
levels(f1)#get levels
