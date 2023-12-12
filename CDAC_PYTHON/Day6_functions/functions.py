#types Of FUnction
#required argument
def add(a,b):
    print(a+b) 

add(10,20)

add(10) TypeError: add() missing 1 required positional argument: 'b'

add() #TypeError: add() missing 2 required positional arguments: 'a' and 'b'


#----------------------------
#Default Arguments

def add(a=5,b=10):
    print(a+b) 

add(10,20)

add(10) 

add()

#----------------------------
#Keyword Arguments type
def add(a=5,b=10):
    print(a+b) 

add(10,20)

add(b=10,a=20)
add(b=10) 

add()

#----------------------
def display(id,name,sal):
    print("EmpId: {} Name: {} SAlary :{}".format(id,name,sal))


display(12,sal=3000,name='Ritesh')

display(sal=3000,name='Ritesh',id=89)



#----------------------Variable Length---------------

def add(a,*b):
    print(type(b))
    print(b)
    sum=a
    for i in b:
        sum += i
    print(sum)

add(12,3,45,6,9)
add(12,3)
add(1,2,3.4,5.6,7)
add('a','b','c')
add([1,2],[3,4,5],[45,67,89,0],[91])

'''
<class 'tuple'>
(3, 45, 6, 9)
75
<class 'tuple'>
(3,)
15
<class 'tuple'>
(2, 3.4, 5.6, 7)
19.0
<class 'tuple'>
('b', 'c')
abc
<class 'tuple'>
([3, 4, 5], [45, 67, 89, 0], [91])
[1, 2, 3, 4, 5, 45, 67, 89, 0, 91]

'''
#------------------------------------
def display(**subjects):
    print(type(subjects))
    for k,v in subjects.items():
        print(k,v)
        
display(c=23,java=40,python=90)
display(java=40)
display(cpp=78,ds=89)


#------------------------------------
#passing dictionary as argument
def displayDict(d):
    print(type(d))
    for i in d.items():
        print(i)

displayDict({1:200,3:90,6:988})


#passing list as argument
def displayDict(d):
    print(type(d))
    for i in d:
        print(i)

displayDict([12,34,56,78,9])

#------------------------------------
#lambda function


sqr = lambda a:a*a
print(sqr(10))

sqr = lambda a=4:a*a
print(sqr(10))
print(sqr())


sum1=lambda a,b:a+b

print(sum1(10,20))
print(sum1(10.4,20))
print(sum1(10.2,20.4))
print(sum1((10,20),(12,2,3)))
print(sum1([10,20],[12,34,56,78]))
print(sum1('asss','bbbbbb'))

#-------------------------------------

sum1=lambda a,*b:a+sum(b)

print(sum1(10,20,34,56))
print(sum1(10.4,20,56,7,8,9))
print(sum1(10.2,20.4,1,2,3,4,5))
print(sum1(10,20))

#-----------------Builtin--------------------

lst=[1,2,3,4,5]
print(sum(lst)) #15

print(abs(-4)) #4

print('23+4') #23+4
print(eval('23+4')) #27

#-------------all and any
s=int(input("enter subscribers"))

l=int(input("enter likes"))

v=int(input("enter views"))

lst=[s>300,l>500,v>1000]
print(lst)

if all(lst):
    print("Excellent channel")
elif any(lst):
    print("Ok ok channel")
else:
    print('Dont watch')
    

#----------------map

def square(n):
    return n*n

lst=[12,3,4,5,6,7,22]

res=map(square,lst)
print(res)
print(list(res))

#--------------------------

lst=[12,3,4,5,6,7,22]

res=map(lambda a:a*a,lst)
print(res)
print(list(res))

#-------------------------
lst=["Pune","Nasik","Amravati","Ratnagiri"]

res=map(len,lst)
print(list(res))

#-------------------------
lst=["Pune","Nasik","Amravati","Ratnagiri"]

res=map(str.upper,lst)
print(list(res))

#-------------------------
lst=["Pune","Nasik","Amravati","Ratnagiri"]

res=map(lambda s:s[:2],lst)
print(list(res))

#-------------------------
lst=["Pune","Nasik","Amravati","Ratnagiri"]

res=map(lambda s:s[::-1],lst)
print(list(res))

#-------------------------Filter

def iseven(n):
    return n%2==0


lst=[12,3,4,5,6,7,22]

res=filter(iseven,lst)
print(res)
print(list(res))


#----------------------------

lst=[12,3,4,5,6,7,22]

res=filter(lambda x:x%2==0,lst)
print(res)
print(list(res))

#-----------------
lst=["Pune","nasik","Amravati","narayangoan","ratnagiri"]

res=filter(str.islower,lst)
print(res)
print(list(res))
#---------------------------------------------

lst=["Pune","nasik","Amravati","narayangoan","ratnagiri"]

res=filter(lambda s:s.startswith("na"),lst)
print(res)
print(list(res))
#---------------------------------------

#Local and Global


def mydunction():
    no=10 #local variable
    print(no)

mydunction()
print(no) #NameError: name 'no' is not defined


#----------------------------

def mydunction():
    no=10 #local variable
    print(no)

no=100 #global
mydunction()
print(no) #100


#----------------------------

def mydunction():
    global no #global variable
    no=10
    print(no)

no=100 #global
mydunction()
print(no) #100
































