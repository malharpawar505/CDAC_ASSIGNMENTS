#Example 1 : 
#print 1 to 10 no
no =1
while no<=10:
    print(no)
    no =no+1

#-------------------------------------
#Example 2 : 
#print table of num
num =int(input("Enter no"))
no =1
while no<=10:
    print(no *num)
    no =no+1

#-------------------------------------
#Example 3 : 
num =int(input("Enter no"))
no =1
while no<=10:
    print(no *num)
    no =no+1
else:
    print("While completed")

#-------------------------------------
#Example 4 : 
#passsword verification
password=12345
cnt = 0

while cnt <3:
    pwd =int(input("Enter password"))
    cnt +=1
    if password == pwd:
        print("Login successfyl")
        break
    else:
        print("wrong password")
else:
    print("Account is blocked")
    
#-------------------------------------
#Example 5 : 
#range function
print(list(range(10))) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print("--------------------")

print(list(range(1,10))) #[1, 2, 3, 4, 5, 6, 7, 8, 9]
print("--------------------")

print(list(range(1,10,2))) #[1, 3, 5, 7, 9]
print("--------------------")

print(list(range(10,-1,-1))) #[10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print("--------------------")

print(list(range(5,16))) #[5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print("--------------------")

print(list(range(0,-10))) #[]

#-------------------------------------
#Example 6 : 
#prints 1 to 10 no
for i in range(1,11):
    print(i)
    
#-------------------------------------
#Example 7 :     
#prints each char in seq
for i in "Welcome":
    print(i)
    
#-------------------------------------
#Example 8 :  
#prints table using for loop   
no = 9
for i in range(1,11):
    print(i*no)

#-------------------------------------
#Example 9 : 
#prints table using for loop   
no = 9
for i in range(1,11):
    print(no,"*",i,"=",i*no)
    
    
#-------------------------------------
#Example 10 : 
#prints pattern
'''
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * * * 

'''
rows = int(input("Enter no of rows"))

for i in range(1,rows):
    for starts in range(i):
        print("*" ,end=" ")
    print()


#-------------------------------------
#Example 10 : 
#prints pattern
'''
1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5 
6 6 6 6 6 6 
7 7 7 7 7 7 7 
8 8 8 8 8 8 8 8

'''

rows = int(input("Enter no of rows"))

for i in range(1,rows):
    for starts in range(i):
        print(i ,end=" ")
    print()

#-------------------------------------
#Example 10 : 
#prints pattern
'''
Enter no of rows7
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 
1 2 3 4 5 6 

'''

rows = int(input("Enter no of rows"))

for i in range(1,rows):
    for starts in range(1,i+1):
        print(starts ,end=" ")
    print()
#-------------------------------------
#Example 11 : 
#Reverse string
s=''
for i in "Welcome":
    s=i+s

print(s)


#-------------------------------------