char = input("Enter string")

match char:
    case 'A':
        print("A character")
    case 'B' | 'C':
        print("B or C char")
    
    case _:
        print("Invalid character")
        
#--------------------------------------


def matchdemo(char):
    
    match char:
        case 1:
            print("A character")
        case 2 | 4:
            print("B or C char")
        case str() if char.startswith("my") :
            print("String is strting with my")
        case _:
            print("Invalid character")
            
matchdemo(1) 
matchdemo(4) 
matchdemo("my name is.....") 
matchdemo("abc")           


#--------------------------------------


def matchdemo(lst):
    
    match lst:
        case [time,name]:
            print(f" Good {time} , {name}")
        case [time,*name]:
            for nm in name:
                print(f" Good {time} , {nm}")
        case _:
            print("Invalid character")
            
matchdemo(["morning","Ajay"]) 
matchdemo(["Afternoon","jay","Vijay","Raju"])        