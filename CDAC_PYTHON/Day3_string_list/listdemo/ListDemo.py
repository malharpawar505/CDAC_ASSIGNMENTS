lst=[]
print(type(lst))

l=[1,2,3,4,5]
l1=["Pune","Delhi","Kolkatta","Goa"]
l2=[100,300,"Sudha","Rama"] #mixed

l3=[10,20,30,[1,2,3,4],"Sarita"] #nested


print(l)
print(l1)
print(l2)
print(l3)

for i in l:
    print(i)
    
for i in range(len(l2)):
    print(l2[i]) 
    
print(l3[0])
print(l3[1])
print(l3[-1])
print(l3[:])
print(l3[1:3])

print(l3[3])

print(l3[3][3]) #4

print(l3[-1][2:4]) #ri


#----------Accept element from user------------------------------
lst=[]
no =int(input("Enter no of elements to add"))

for i in range(no):
    ele = input("enter ele")
    lst.append(ele)
    
print(lst)


lst.append("Pune")

print(lst)


lst.insert(3,"Rutu")
print(lst)

lst.insert(-1,"keshav")
print(lst)
#------------------Update

lst[0]="Mohan"
print(lst)



lst[1:3]=56,789
print(lst)


#------------------Delete
del lst[0]
print(lst)

del lst[1:3]
print(lst)


del lst
print(lst) #error NameError: name 'lst' is not defined


#------------------Delete Built in Methods

l3=[10,20,30,[1,2,3,4],"Sarita"]

ele= l3.pop()
print(ele)
print(l3)



ele= l3.pop(1)
print(ele)
print(l3)

l3.remove(30) #remove by val

print(l3)

l3.clear()
print(l3)


#------------------

#------------List Operators

l1=[1,20]
l2=[100,600]

print(l1+l2)
print(l1*3)

l3=[1,2,3,4,5]
no =3
print(no in l3) #true

no =[1,2]
print(no in l3) #False

l3=[10,[1,2],3,4,5]
no =[1,2]
print(no in l3) #True


#-----------Identity

l=[1,2]
l1=[1,2]
l2=l
l3=l[:]


print(l is l1)#False
print(l is l2) #True
print(l is l3)#False

print(l == l1)#True
print(l == l2)#True
print(l == l3)#True


print(id(l))
print(id(l1))
print(id(l2))
print(id(l3))
#---------------
s="Hi"
s1="Hi"
s2=s
s3=s[:]


print(s is s1)
print(s is s2)
print(s is s3)

print(s == s1)
print(s == s2)
print(s == s3)



print(id(s))
print(id(s1))
print(id(s2))
print(id(s3))

#------------------------------list function

l=[10,400,20,4,30,40,50,1]

print(len(l))
print(min(l))
print(max(l))

t=(10,20,30)
lst=list(t)
print(lst)

#-------------Remove duplicate ele from list
l=[10,400,20,4,30,40,50,1,10,4,20]

print(list(set(l)))

#--------------------List methods
print(dir(list))
l=[10,400,20,4,30,40,50,1,10,4,20]
print(l.count(10))


l1=[200,300]

l.extend(l1)
print(l)

l.reverse()
print(l)

l.sort()
print(l)


print(l.index(50))#9


print(l.index(500)) #ValueError: 500 is not in list

l3=l.copy()

print(id(l3))
print(id(l))
#-------------------------------------------------













