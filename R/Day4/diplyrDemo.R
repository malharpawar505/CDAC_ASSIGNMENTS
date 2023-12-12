library("xlsx")
df<- read.xlsx("C:\\Snehal\\CDAC\\Sept 23\\DBDA\\R\\Day4\\Order_data.xlsx",1)
df

library("tidyverse")
tbl <- as_tibble(df)
tbl


mtcars
tbl <- as_tibble(mtcars)
tbl
#----------------------------------------
#arrange
arrange(tbl,Region)

arrange(tbl,desc(Region))

arrange(tbl,desc(Region),cust)


arrange(tbl,desc(Units))

df1<-arrange(df,desc(Units))
df1
#----------------------------------------------------------
#Select

df2<- select(tbl,order.no,cust,Item)
df2


df2<- select(tbl,2:5)
df2


df2<- select(tbl,OrderDate:cust)
df2

df2<- select(tbl,"OrderDate":"cust")
df2

df2<- select(df,order.no,cust)
df2

df2<- select(df,c(order.no,cust,Units))
df2

df2<- select(df,-c(order.no,cust,Units))
df2

df2<- select(df,starts_with("Unit"))
df2

df2<- select(df,ends_with("st"))
df2

#----------------------------------------
#filter
df3<- filter(tbl,Region=="East")
df3

df3<- filter(tbl,Region=="East" & Unit.Cost< 10)
df3

df3<- filter(tbl,Region=="East" | Unit.Cost< 10)
df3


df4<-select(tbl,Region,Item,Units,Unit.Cost)
df4

df5<-filter(df4,Region=="East" & Unit.Cost< 10)
df5

df5<-filter(select(tbl,Region,Item,Units,Unit.Cost),Region=="East" & Unit.Cost< 10)
df5

#-------- ------------------------------------------------------
# %>% Pipe Operator

df6<- tbl %>%
      select(Region,Item,Units,Unit.Cost)%>%
      filter(Region=="East" & Unit.Cost< 10)
df6
#-----------------------------------------------
df6<- tbl %>%
  select(Region,Item,Units,Unit.Cost)%>%
  filter(Region=="East" & Unit.Cost< 10)%>%
  arrange(Unit.Cost)
df6
#-----------------------------------------------
df6<- tbl %>%
  select(Region,Item,Units,Unit.Cost)%>%
  filter(Region=="East" & Unit.Cost< 10)%>%
  arrange(desc(Unit.Cost))
df6
#-----------------------------------------------
df6<- tbl %>%
  select(Region,Item,Units,Unit.Cost)%>%
  filter(Item %in% c("Pencil","Pen") )%>%
  arrange(desc(Unit.Cost))
df6

#---------------------------------------------------
#rename
#rename the columns/Variables -newname=oldname
df3<- rename(tbl,"UnitCost"="Unit.Cost","no"="order.no")
df3
#----------------------------------------------
#Mutate
#Add new Columns
df4<- mutate(tbl,"dist_tot"=(Total - Total*0.05))
df4
select(df4,3:9)

#----------------------------------------------
df7<- summarise(tbl, "sum"= sum(Total))
df7

df7<- summarise(tbl, "sum"= mean(Total))
df7

df7<- summarise(tbl, "max"= max(Total))
df7

#--------------------------------------------------
# Sample data
students <- data.frame(
  student_id = c(1, 2, 3, 4, 5, 6, 7, 8),
  subject = c("Math", "Science", "Math", "Science", "Math", "Science", "Math", "Science"),
  score = c(85, 78, 92, 88, 75, 81, 90, 85)
)

# Display the original data
print(students)


# Grouping by subject and calculating the average score for each subject
average_scores <- students %>%
  group_by(subject) %>%
  summarise(avg_score = mean(score))

# Display the average scores
print(average_scores)

#---------------------------------------------------------------
avg_scr <- summarise(group_by(students,subject),avg_score=mean(score))
avg_scr

max_scr <- summarise(group_by(students,subject),mx_score=max(score))
max_scr

#-----------------------------------------------------------

