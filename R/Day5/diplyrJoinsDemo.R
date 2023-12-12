library("tidyverse")
id<-c(1,2,3,4)
nm<-c("a","b","c","d")
df<-data.frame(id,nm)
df



id<-c(1,2,4,5)
age<-c(12,45,67,89)
df1<-data.frame(id,age)
df1

inner_join(df,df1,by="id")
left_join(df,df1,by="id")
right_join(df,df1,by="id")
full_join(df,df1,by="id")
