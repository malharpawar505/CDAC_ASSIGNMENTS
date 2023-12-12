setwd("C:\\Snehal\\CDAC\\Sept 23\\DBDA\\R\\Day3\\ds")

df <- read.csv("pizza.csv") 
df

df1<-df[df$Sales<1000,]
df1

write.csv2(df1,"pizza1.csv")

write.csv(df1,"pizza2.csv")
#-------------------------------------------
df <- read.csv2("pizza1.csv") 
df

#-------------------------------------------
df <-read.table("members.txt",header = T,skip=1)
df

#---------------------
df <-read.table("members.txt",header = F,skip=1)
df

#-----------------------------------
df <-read.table("Pen.txt",header = T)
df

df[,-2]
#-----------------------------------
install.packages("xlsx")
library("xlsx")
df<-read.xlsx("quality.xlsx",1)
df

df1<-read.xlsx("quality.xlsx",2)
df1




