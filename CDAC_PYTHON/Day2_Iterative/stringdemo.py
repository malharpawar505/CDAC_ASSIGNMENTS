s="Snehal 'welcome'"
s1= 'hi "student" '
s2=''' line1
  line 2
  line3'''
s3=""" Line1
 line 2
line3"""

print(s)
print(s1)
print(s2)
print(s3)

print("----------------------------------")
s="Welcome"
for i in s:
    print(i)

print("----------------------------------")

#s[0]='h' #error  'str' object does not support item assignment
s="Hello World" #entire replacement
print(s)

print("----------------------------------")
#del s[0] #error   'str' object doesn't support item deletion
del s  #delete entire string
print(s)  #NameError: name 's' is not defined.


 
