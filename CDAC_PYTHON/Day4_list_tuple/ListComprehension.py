#list Comprehenssion
l1=[1,2,3,4,12,45,67,32,4,12,45,67]
print(l1)

l2=[x for x in l1]

l3=[x **2 for x in l1]

print(l2)
print(l3)

#create 1 to 100 list
l4=[m for m in range(1,101)]
print(l4)


#Create Odd list
l5=[m for m in range(1,101) if m%2==1]
print(l5)


#Nested List comprehenssion
col=['Red','Green']
things=['House','Car']


combo=[(x,y) for x in col for y in things]
print(combo)


combo=[[x,y] for x in col for y in things]
print(combo)


#------------------------------------------

a,b,c = 10,20,30
print(a,b,c)

a,*b=10,20,30
print(a)
print(b)



*a,b=10,20,30
print(a)
print(b)


a,*b,c=10,20,30,40,50
print(a)
print(b)
print(c)


















