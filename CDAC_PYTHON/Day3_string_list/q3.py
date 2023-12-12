a="HelloWorld"
count=0
cou=0
vowels="aeiou"
for i in a.lower():
    if i.isalpha():
        if i in vowels:
            count+=1
        else :
            cou+=1
else:
    print(count,cou)
            
