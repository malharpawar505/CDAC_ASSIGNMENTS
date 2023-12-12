#Membership operator
s="Welcome Student"
print(s)


print("el" in s)

print("tt" in s)

print("-------String Formating--------")
#1

print("Hello %s having %d and salary is %f ....%.2f "%("Raghu",56,234.956,234.956))

print("-------String Formating using format Method--------")

#1 Default
print("\n-------String Formating using format Default--------")
print("My DBDDA students are {} {} and {}".format("smart","clever","Hardworking"))


#2 Positional
print("\n-------String Formating using format positional--------")
print("My DBDDA students are {0} {1} and {2}".format("smart","clever","Hardworking"))
print("My DBDDA students are {1} {2} and {0}".format("smart","clever","Hardworking"))
print("My DBDDA students are {2} {2} and {2}".format("smart","clever","Hardworking"))




#3 Keyword
print("\n-------String Formating using format keyword--------")
print("My DBDDA students are {s} {h} and {c}".format(s="smart",c="clever",h="Hardworking"))


print("\n -------String Formating--------")

name=input("Enter name")
age = int(input("Enter age"))

print(f"Hello {name} you are {age} years old. {34+5+6}")

