nm<-c("a","b","c","d","e","f")
age<-c(23,15,17,12,34,16)
marks<-c(56.7,90.6,36.0,67.45,90.6,36.0)

df<-data.frame(nm,age,marks)
df

summary(df)
length(df)
str(df)

colnames(df) #get colnames of df

names(df) #get colnames of df

df

#Subsetting the df
df[1,1]
df[1,]
df[1,c(2,3)]#1st row age and Marks col
df[ ,c(2,3)]#all row age and Marks col
df$age

df[df$age>15,] #filter data 
attach(df)
df[age>15,] #no need to use df$ after attach 

df[marks==36.0,]

rm(df) #remove df from memory

df[which(marks>40),]

df[which(df$marks>40),]


df[which(marks>40 & age< 20),]

df[which(marks==90.60 | age< 20),]

df[which(marks==90.60 | age< 20),1]

df[which(marks==90.60 | age< 20),c(1,2)]


subset(df,marks>40)


subset(df,marks>40,select = c(nm,age))#Select cols


subset(df,marks>40 & age <20 ,select = c(nm,age))
#-----------------------------------------------------
detach(df) #detach df 
df
rm(df) #remove df from memory
df #error
#-----------------------------------------------------------
data()
df=cars
df

df=mtcars
df

colnames(df)
names(df)
#-----------------------------------------------------------
df<-read.csv("C:\\Snehal\\CDAC\\Sept 23\\DBDA\\R\\Day3\\ds\\Salaries.csv")
df

names(df)
summary(df)


df[df$salary <80000 & df$salary > 70000,c(1,4,6)]
#-----------------------------------------------
setwd("C:\\Snehal\\CDAC\\Sept 23\\DBDA\\R\\Day3\\ds\\")
df<-read.csv("Cars2018.csv")
df
names(df)

getwd() #"C:/Snehal/CDAC/Sept 23/DBDA/R/Day3/ds"
