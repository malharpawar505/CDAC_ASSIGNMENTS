s={1,2,3,4,5}
print(s)
print(type(s))
#{1, 2, 3, 4, 5}
#<class 'set'>


s={1,2,3,4,5,2,3,2}
print(s)
#{1, 2, 3, 4, 5}
#duplicate values are not allowed

s={1,2,3,4,5,38,40,56,78}
print(s)
for i in s:
    print(i)
    
#unorder collection
'''
{1, 2, 3, 4, 5, 38, 40, 78, 56}
1
2
3
4
5
38
40
78
56
'''
#------------------

s={1,2}
s.add(10)#add element
s.add(20)
print(s) 

l=[1,2,3,4]
s= set(l)
print(s)

l=[1,2,3,4]
s= frozenset(l)
print(s)
print(type(s))
s.add(10) #AttributeError: 'frozenset' object has no attribute 'add'

#----------------function
s={1,2,3,4,5,38,40,56,78}
print(s)
print(len(s))
print(min(s))
print(max(s))
#{1, 2, 3, 4, 5, 38, 40, 78, 56}
#9
#1
#78


#----------------Methods

s={10,20,30,40,50}
s1={40,50,60,70,80}


print(s.difference(s1)) #{10, 20, 30}
print(s1.difference(s)) #{80, 60, 70}


print(s.intersection(s1)) #{40, 50}

print(s.union(s1)) #{70, 40, 10, 80, 50, 20, 60, 30}
















