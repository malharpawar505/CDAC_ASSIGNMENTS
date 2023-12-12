#string Functions..............

s="Helloworld"
print(len(s))
print(max(s))
print(min(s))


print("\n Before Converting")
num=12345
print(num)
print(type(num))
num=str(num)

print("After Converting")
print(num)
print(type(num))


#String Methods................

s="Welcome student"
s1="Hello WORLD"
print(s.capitalize())
print(s.title())
print(s.swapcase())
print(s.upper())
print(s.lower())

print("\n-------------Find------")
print(s.find("co"))
print(s.find("xy"))
print(s.find("e"))
print(s.rfind("e"))
print(s.rfind("xy"))

print("\n-------------index------")
print(s.index("co"))
print(s.index("xy")) #error
print(s.rindex("co"))
print(s.rindex("xy")) #error


print(s.count("e"))
print(s.startswith("We"))
print(s.startswith("wex"))

print(s.endswith("nt"))
print(s.endswith("wex"))

print(s.replace("e","x"))


print("1123".isdigit())

print("as123".isdigit())
print("1123df".isalpha())
print("1123df".isalnum())
print("hjhjdf".isalpha())
print(" vv ".isspace())
print("  ".isspace())

print("Wel Come".istitle())
print("Wel Come".isupper())
print("WEL".isupper())
print("WEl".islower())
print("wel".islower())


cntu=0
cntl=0
s="hjTYU njn"
for i in s:
    if i.isupper():
        cntu+=1
    elif i.islower():
        cntl+=1
else:
    print("Count of UPPercase ", cntu)
    print("Count of Lowercase ", cntl)


#------------------------------------
cntalpha=0
cntdigit=0
s="hjTYU 12 nj67n"
for i in s:
    if i.isalpha():
        cntalpha+=1
    elif i.isdigit():
        cntdigit+=1
else:
    print("Count of Alpha ", cntalpha)
    print("Count of Digits ", cntdigit)




#------------------------------------
cntVowels=0
cntConso=0
s="hjTaYeU 12 nj6io7n"
vowels="aeiou"
for i in s.lower():
    if i.isalpha():
        if i in vowels:
            cntVowels +=1
        else:
            cntConso+=1        
else:
    print("Count of Vowels ", cntVowels)
    print("Count of Consonents ", cntConso)


#------------------------------------

s="hi students how r you?"
lst = s.split();
print(lst)

s="hi students how r you?"
lst = s.split('e');
print(lst)


lst=["Pune","Mumbai","Goa","Nagar"]
s="-->".join(lst)
print(s)


tup=('1','2','3')
s="-->".join(tup)
print(s)



