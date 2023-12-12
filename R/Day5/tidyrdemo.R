table4a

#---------------------------------------
#gather

gather(table4a,key="year",value = "cases",-country)

#or
gather(table4a,'1999','2000',key="year",value = "cases")

#or

table4a %>%
  gather(key="year",value = "cases",-country)
#-----------------------------------------------
wide_data <- data.frame(
  id = 1:3,
  t1_score = c(85, 90, 78),
  t2_score = c(88, 92, 80),
  t3_score = c(90, 95, 82)
)
wide_data

long_d <- gather(wide_data,key="time",value = "score",-id)
long_d
#-----------------------------------------------
#Spread

table2
short_d<- spread(table2,key="type",value="count")
short_d
#--------------------------

long_data <- data.frame(
  id = c(1, 1, 2, 2, 3, 3),
  time_period = c("t1", "t2", "t1", "t2", "t1", "t2"),
  score = c(85, 88, 90, 92, 78, 80)
)
long_data

spread(long_data,key = "time_period",value = "score")


#--------------------------
#Seperate

table3

df1<- separate(table3,rate,into=c("cases","population"),sep="/")
df1

#Convert data into int /expected datat type
df1<- separate(table3,rate,into=c("cases","population"),sep="/",convert = T)
df1


df2<- separate(table3,year,into=c("century","yr"),sep=2,convert = T)
df2


# Sample data
data <- data.frame(
  id = 1:3,
  name_age = c("Alice_25", "Bob_30", "Charlie_28")
)
data

data1<-separate(data,name_age,into=c("name","age"),sep="_")
data1
#-------------------------------------------------------------------
#Unite
table5

unite(table5,"newYear",century,year,sep="")

df3<- unite(data1,"nm_age",name,age,sep="$")
df3

#------------------------------------------------------------------
#Complete

# Sample incomplete data
data <- data.frame(
  gender = c("Male", "Female", "Female"),
  product = c("A", "B", "C"),
  value = c(10, 20, 15)
)

data

#Complete data with NA
complete(data,gender,product)

complete(data,gender,product,fill=list(value=0))

#------------------------------------------------------------------
#Fill
# Sample data with missing values
data <- data.frame(
  id = c(1, 1, 2, 2, 3, 3),
  value = c(5, NA, 7, NA, 3, NA)
)
data

fill(data,value,.direction = "down")

fill(data,value,.direction = "up")

#------------------------------------------------------------------