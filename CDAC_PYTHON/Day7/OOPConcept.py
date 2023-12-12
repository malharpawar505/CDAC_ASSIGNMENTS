#class emp
class emp:
    pass

e= emp() #Object of emp created
print(type(e))
print(id(e))

#-----------------------------
#class emp
class emp:
    '''This is documentation of emp'''
    pass

e= emp() #Object of emp created
print(type(e))
print(id(e))
print(emp.__doc__)
print("Help: ",help(emp))


#-------------Instance Variables----------------
#1 
class emp:
    pass

e=emp()
e.fname="Riya"
e.lname='XYZ'

e1=emp()
e1.bonus= 8000
e1.mgr='Keshav'

print(e.fname, e.lname) #Riya XYZ
print(e.bonus,e.mgr) #AttributeError: 'emp' object has no attribute 'bonus'
print(e1.bonus,e1.mgr) #8000 Keshav
#print(e1.fname, e1.lname) #AttributeError: 'emp' object has no attribute 'fname'


#-------------Instance Variables----------------
#2 

class emp:
    eno=0
    name='default'
    

e=emp()
e1=emp()
e2=emp()

print(e.eno,e.name)
print(e1.eno,e1.name)
print(e2.eno,e2.name)
print("-"*30)
emp.eno =10
emp.name="No Name"
print(e.eno,e.name)
print(e1.eno,e1.name)
print(e2.eno,e2.name)
print("-"*30)

e.eno=100
e.name="Pallavi"

print(e.eno,e.name)
print(e1.eno,e1.name)
print(e2.eno,e2.name)
print("-"*30)
emp.eno =56
emp.name="--------"

print(e.eno,e.name)
print(e1.eno,e1.name)
print(e2.eno,e2.name)

'''
0 default
0 default
0 default
------------------------------
10 No Name
10 No Name
10 No Name
------------------------------
100 Pallavi
10 No Name
10 No Name
------------------------------
100 Pallavi
56 --------
56 --------
'''

#-----------------Method----
class emp:
    eno=0
    name='default'
    
    #method in python
    def display(self):
        print(self.eno,self.name)

e=emp()
e1=emp()
e2=emp()

e.display() #emp.display(e)
e1.display()
e1.display()


#-----------Instance variables using Method
class emp:
    eno=0
    name='default'
    
    def setBonus(self,bns):
        self.bonus = bns
        
    def getBonus(self):
        return self.bonus
    
    #method in python
    def display(self):
        print(self.eno,self.name)

e=emp()
e1=emp()
e2=emp()
e.display() #emp.display(e)
e1.display()
e1.display()

print(e.bonus) #AttributeError: 'emp' object has no attribute 'bonus'

e.setBonus(5000)
print(e.bonus) #5000
print(e.getBonus()) #5000


#-------------------------------
class emp:
    eno=0
    name='default'
    
    def setBonus(self,bns):
        self.bonus = bns
        
    def getBonus(self):
        return self.bonus
    
    #method in python
    def display(self):
        print(self.eno,self.name)

e=emp()
e.setBonus(5000)
e.display() #emp.display(e)

#e1.display() #AttributeError: 'emp' object has no attribute 'bonus'

if hasattr(e, "bonus"):
    print(e.bonus)
else:
    print("No attribute")


if hasattr(e1, "bonus"):
    print(e1.bonus)
else:
    print("No attribute")


print(getattr(e, "bonus"))#5000
print(getattr(e1, "bonus")) #AttributeError: 'emp' object has no attribute 'bonus'

#-----------------------Constructor


class emp:
    
    #constructor
    def __init__(self):
        print("No args constructor")

e= emp() #No args constructor


#--------------------
class emp:
    
    #constructor
    def __init__(self):
        print("No args constructor")
        
    def __init__(self,no,name):
        print("args constructor")
        self.eno=no
        self.ename= name

e= emp() #TypeError: emp.__init__() missing 2 required positional arguments: 'no' and 'name'
e1= emp(10,"Kishori")


#--------------------
class emp:
    
            
    def __init__(self,no=0,name='default'):
        print("args constructor")
        self.eno=no
        self.ename= name
        
    def display(self):
        print(self.eno , self.ename)
        
        
        
e= emp() #TypeError: emp.__init__() missing 2 required positional arguments: 'no' and 'name'
e1= emp(10,"Kishori")

e.display()
e1.display()

#--------------------
class emp:
    
    location="Pune"        
    def __init__(self,no=0,name='default'):
        print("args constructor")
        self.eno=no
        self.ename= name
        
    def display(self):
        print(self.eno , self.ename,self.location)
        
        
        
e= emp() #TypeError: emp.__init__() missing 2 required positional arguments: 'no' and 'name'
e1= emp(10,"Kishori")
e1.location="Ratnagiri"
e.display()
e1.display()
print("-------After Location change---------")
emp.location="Mumbai"
e.display()
e1.display()


#--------------------
class emp:
    
    location="Pune"        
    def __init__(self,no=0,name='default'):
        print("args constructor")
        self.eno=no
        self.ename= name
        
    #Destructor 
    def __del__(self):
        print("object Destroyed...")
        
    def display(self):
        print(self.eno , self.ename,self.location)
        


e = emp()
e.display()
del e
e.display() #NameError: name 'e' is not defined


#--------------------
class emp:
    
    location="Pune"        
    def __init__(self,no=0,name='default'):
        print("args constructor")
        self.eno=no
        self.ename= name
        
    #Destructor 
    def __del__(self):
        print("object Destroyed...")
        
    def display(self):
        print(self.eno , self.ename,self.location)
        
    def __str__(self):
        return f"Employee eno={self.eno} ename: {self.ename}"


e=emp()
print(e)

e1=emp(1,"Rajiv")
print(e1)

e2=emp(100,"Rutuja")
print(e2)

#--------------------list of obj
class emp:
    
    location="Pune"        
    def __init__(self,no=0,name='default'):
        #print("args constructor")
        self.eno=no
        self.ename= name
            
    def display(self):
        print(self.eno , self.ename,self.location)
        
    def __str__(self):
        return f"Employee eno={self.eno} ename: {self.ename}"


e=emp()
e1=emp(1,"Rajiv")
e2=emp(100,"Rutuja")


lst=[e,e1,e2]
for i in lst:
    print(i)

for i in lst:
    i.display()

lstemp=[]
#create 3 objects
for i in range(3):
    eno=int(input("Enter eno"))
    ename=input("Enter name")
    e=emp(eno,ename)
    lstemp.append(e)
    
for i in lstemp:
    print(i)

for i in lstemp:
    i.display()    


#----------------Class Method--------------

class emp:
    
    location="Pune"        
    def __init__(self,no=0,name='default'):
        #print("args constructor")
        self.eno=no
        self.ename= name
            
    def display(self):
        print(self.eno , self.ename,self.location)
        
    def __str__(self):
        return f"Employee eno={self.eno} ename: {self.ename}"

    #class Method
    def myMethod(): 
        print("I am in My method.this class Method")
        
        
        
e = emp()
e.myMethod() #emp.myMethod(e)
#TypeError: emp.myMethod() takes 0 positional arguments but 1 was given

#class Method
emp.myMethod()