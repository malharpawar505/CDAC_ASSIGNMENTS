a=input("Enter String")
count=0
cou=0
for i in a:
    if i.isupper():
        count+=1
    else :
        cou+=1
print("Upper::",count,"Lower::",cou)
