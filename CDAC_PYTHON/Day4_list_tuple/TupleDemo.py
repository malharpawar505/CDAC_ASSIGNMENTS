
t=() #Empty tuple
print(t)
print(type(t))



t=(10,) #Single tuple
print(t)
print(type(t))




t=10,20,30,40
print(t)
print(type(t))



t1=(10,20,30,40)
print(t1)
print(type(t1))


a,b,c=10,"Ritesh",345.78
t2=(a,b,c)
print(t2)
print(type(t2))

#------------------------------------------------
print(t1)
t1[0]=100 #TypeError: 'tuple' object does not support item assignment

del t1[0] #TypeError: 'tuple' object doesn't support item deletion

#update entire tuple
t1=(20,30)
print(t1)
print(type(t1))


#delete entire tuple
print(t1)
del t1
print(t1) #NameError: name 't1' is not defined

#------------------------------------------------
t1=(20,30,40,50)
t2=(1,2,3)

print(t1+t2) #Concatination

print(t1*3) #repitation
print(t1[1])
print(t1[1:])

print(t1==t2)

print(30 in t1) #membership operators

#------------------------Function------------------------
t1=(5,67,100,500,20,30,40,1,50)

print(len(t1))
print(min(t1))
print(max(t1))
l1=['a','v','t']
print(tuple(l1))

#------------------------Methods------------------------


t1=(5,67,100,500,20,30,40,1,50,1,20,30,40,1)

print(t1.count(1))

print(t1.index(100))

print(t1.index(1000)) #ValueError: tuple.index(x): x not in tuple



#------------------------------------------------

















