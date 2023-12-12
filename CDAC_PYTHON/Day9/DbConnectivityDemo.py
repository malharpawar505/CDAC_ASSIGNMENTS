

#Step 1
import mysql.connector


#step2
con = mysql.connector.connect(host="localhost",
                              user="root",password="12345",
                              auth_plugin='mysql_native_password')

#step3

cur = con.cursor()


#step4

cur.execute("show databases")

#Displaying data
for db in cur:
    print(db)
    

#step5
cur.close()
con.close()

#---------------------------------------------------------
#create DB
#Step 1
import mysql.connector


#step2
con = mysql.connector.connect(host="localhost",
                              user="root",password="12345",
                              auth_plugin='mysql_native_password')

#step3

cur = con.cursor()


#step4

cur.execute("create database pythondbtest")


#step5
cur.close()
con.close()


#---------------------------------------------------------
#create Table in Db
#Step 1
import mysql.connector


#step2
con = mysql.connector.connect(host="localhost",
                              user="root",password="12345",
                              database='pythondbtest',
                              auth_plugin='mysql_native_password')

#step3

cur = con.cursor()


#step4

cur.execute("create table cust(cid int AUTO_INCREMENT primary key,cname varchar(100),address varchar(200))")


#step5
cur.close()
con.close()
#---------------------------------------------------------
#show Tables
#Step 1
import mysql.connector


#step2
con = mysql.connector.connect(host="localhost",
                              user="root",password="12345",
                              database='pythondbtest',
                              auth_plugin='mysql_native_password')

#step3

cur = con.cursor()


#step4

cur.execute("show tables")

#Displaying data
for db in cur:
    print(db)
    

#step5
cur.close()
con.close()

#---------------------------------------------------------
#Insert Data in Cust
#Step 1
import mysql.connector


#step2
con = mysql.connector.connect(host="localhost",
                              user="root",password="12345",
                              database='pythondbtest',
                              auth_plugin='mysql_native_password')

#step3

cur = con.cursor()


#step4

sql= "insert into cust(cname,address) values(%s,%s)"
val=('Rohit',"Pune")
cur.execute(sql,val)

con.commit()
print("record inserted ",cur.rowcount)

#step5
cur.close()
con.close()