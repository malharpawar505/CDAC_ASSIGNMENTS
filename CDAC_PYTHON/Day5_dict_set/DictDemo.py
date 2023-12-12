d={} #empty Dict
print(d)
print(type(d))

#----------------Add/Update

d={1:10,2:30,3:"Radha",4:[10,20,30]}
print(d)

d[5]="Ratan" #add
print(d)


d[5]="Rohan" #Update
print(d)

d.update({1:20,6:100}) #add,update,merge
print(d)

d1={700:1000,67:300}

d.update(d1)
print(d)

#-----------------------------------
d={1:10,2:30,3:"Radha",4:[10,20,30]}
d1={700:1000,67:300}

d3={**d,**d1}

print(d)
print(d1)
print(d3)

#---------------------
d={k:k**2 for k in range(1,31)}

print(d)


d={k:[k**2,k**3] for k in range(1,31)}

print(d)


#------------Delete---------

d= {1: 20, 2: 30, 3: 'Radha', 4: [10, 20, 30], 5: 'Rohan', 6: 100}

del d[3] #delte Single ele
print(d)


del d #entire d will be deleted
print(d) #NameError: name 'd' is not defined



d= {1: 20, 2: 30, 3: 'Radha', 4: [10, 20, 30], 5: 'Rohan', 6: 100}
s= d.pop(4)
print(s) #hold deleted value
print(d) #After deletion

s= d.popitem()#delete last Item
print(s) #hold deleted key value as tuple
print(d) #After deletion

d.clear()
print(d)
#----------------Display -----

d= {1: 20, 2: 30, 3: 'Radha', 4: [10, 20, 30], 5: 'Rohan', 6: 100}

#1
print(d)

#2 only kys
for i in d:
    print(i)
    
    
#3 only values
for i in d:
    print(d[i])


#4 only keys
for i in d.keys():
    print(i)


#5 only Values
for i in d.values():
    print(i)
    
    
    
 
#6 only key,value tuple
for i in d.items():
    print(i)   
    
    

#7 only key,value 
for k,v in d.items():
    print(k,v)       
    
    
#----------------Operators -----  

#[] -Insert/Update/Display 

print(d[3]) 

d2={1:10,2:20}

d1= d2
print(d2==d1)    

print(1 in d2) #true
print(10 in d2)#false

#---------------------------------
    
d={}
for i in range(3):
    key= input("Enter key")
    val= input("Enter val") #accept string val
    #d[key]= val  
    #or
    d.update({key:val})
   
print(d)    
    
#---------------------------------
    
d={}
for i in range(3):
    key= input("Enter key")
    val= input("Enter val").split() #accept list
    #d[key]= val  
    #or
    d.update({key:val})
   
print(d)  #{'10': ['12', '34', '56', '78'], '23': ['90', '12', '34'], '5': ['89', '76']}  
    
#----------------functions-----------------

d= {1: 20, 2: 30, 3: 'Radha', 4: [10, 20, 30], 50: 'Rohan', 6: 100}

print(len(d))
print(min(d))
print(max(d))

d1=dict([(1,10),(2,20),(3,30),(4,40)])

print(d1)
#----------------------Methods

d1= d.copy()
print(d)
print(d1)
#{1: 20, 2: 30, 3: 'Radha', 4: [10, 20, 30], 50: 'Rohan', 6: 100}

#{1: 20, 2: 30, 3: 'Radha', 4: [10, 20, 30], 50: 'Rohan', 6: 100}



l=['a','b','c']
d1 = d.fromkeys(l)
print(d1) #{'a': None, 'b': None, 'c': None}


l=['a','b','c']
d1 = d.fromkeys(l,30)
print(d1) #{'a': 30, 'b': 30, 'c': 30}

#--------------------------
print(d1)
s = d1.setdefault("c","100")
print(s)
print(d1)



print(d1)
s = d1.setdefault("p","100")
print(s)
print(d1)

#----------------------------------

print(d1) #{'a': 30, 'b': 30, 'c': 30, 'p': '100'}
d1.update({"q":d1.pop('p')})

print(d1)


#{'a': 30, 'b': 30, 'c': 30, 'p': '100'}
#{'a': 30, 'b': 30, 'c': 30, 'q': '100'}

#----------------------------------


l1=[1,2,3,4,5]
l2=[10,20,30,40,50]

d= dict(zip(l1,l2))
print(d) #{1: 10, 2: 20, 3: 30, 4: 40, 5: 50}

#-----------------------------

#default value of strict is false
#strict=False


l1=[1,2,3,4,5]
l2=[10,20,30,40,50,78,90]

d= dict(zip(l1,l2))
print(d)

#--------------------------
l1=[1,2,3,4,5]
l2=[10,20,30,40,50,78,90]

d= dict(zip(l1,l2,strict=True))
print(d) #ValueError: zip() argument 2 is longer than argument 1

#-------------------------------------
d= {1: 20, 2: 30, 3: 'Radha', 4: [10, 20, 30], 50: 'Rohan', 6: 100}

print(d)
print(sorted(d)) #[1, 2, 3, 4, 6, 50]

print(list(reversed(d))) #[6, 50, 4, 3, 2, 1]



print(dict(list(reversed(d.items()))) )

print(dict(list(sorted(d.items()))) )













