no1= int(input("Enter No1"))
no2= int(input("Enter No2"))
print(no1/no2)

#-----------------------------------
try:
    no1= int(input("Enter No1"))
    no2= int(input("Enter No2"))
    print(no1/no2)
except:
    print("Error Occured")
    

#-----------------------------------
try:
    try:
        no1= int(input("Enter No1"))
        no2= int(input("Enter No2"))
    except:
        print("Wrong Input")
    print(no1/no2)
except:
    print("Error Occured while calculation")
    
#-----------------------------------
try:
    try:
        no1= int(input("Enter No1"))
        no2= int(input("Enter No2"))
    except ValueError as e:
        print("Wrong Input ",e )
    print(no1 , no2)
    print(no1/no2)
except ZeroDivisionError as e:
    print("Error Occured while calculation",e)
    
    
#-----------------------------------
try:
    no1= int(input("Enter No1"))
    no2= int(input("Enter No2"))
    print(no1/no2)
 
except ValueError as e:
    print("Value error: ",e)
except ZeroDivisionError as e:
    print("Error Occured while calculation: ",e)
except Exception as e:
    print(e)     
    
#-----------------------------------
try:
    no1= int(input("Enter No1"))
    no2= int(input("Enter No2"))
    print(no1/no2)
except (ValueError,ZeroDivisionError,Exception )as e:
    print(e)      
#-----------------------------------
try:
    no1= int(input("Enter No1"))
    no2= int(input("Enter No2"))
    print(no1/no2)
except (ValueError,ZeroDivisionError,Exception )as e:
    print(e)      
else:
    print("No error")
    
#-----------------------------------

while(True):
     try:
         no1= int(input("Enter No1"))
         no2= int(input("Enter No2"))
         res=no1/no2
     except Exception as e:
        print(e)
        print("Pls enter values again")
     else:
         print(res)
         break
#-----------------------------------

while(True):
     try:
         no1= int(input("Enter No1"))
         no2= int(input("Enter No2"))
         res=no1/no2
     except Exception as e:
        print(e)
        print("Pls enter values again")
     else:
         print(res)
         break
     finally:
         print("I am always executed.....")
    
    
#-----------------------------------
try:
    print("In try")
    no=int(input("no"))
finally:
      print("In finally")
    
#-----------------------------------    
def displaydict(d,k,val):
    try:
        res=d[k]
    except:
        print("New ele is added")
        d[k]=val
    else:
        print(res)
    finally:
        print(d)

displaydict({1:10,2:20},2,100)
displaydict({1:10,2:20},5,100)
    
#-----------------------------------   

#raise
try:
    age=int(input("Enter age"))
    if age< 18:
        raise Exception("Invalid age")
except Exception as e:
    print(e)
else:
    print("Welcome User")    
    
#-----------------------------------   

class NoTooShort(Exception):
    pass

class NoTooLong(Exception):
    pass


magicno=677
cnt=0

while(True):
    try:
        cnt +=1
        no = int(input("enter no: "))
        if no > magicno:
            raise NoTooLong("No is bigger than expected")
        elif no < magicno:
            raise NoTooShort("No is Smaller than expected")

    except Exception as e:
        print(e)
    else :
        print("You WIn.....")
        break
    
    finally:
        print("No of Tries....",cnt)



#----------------------------------- 
print(Exception.__subclasses__())  






   
    