class emp:
    pass

class mgr(emp):
    pass



e= emp()
m= mgr()

print(isinstance(e, emp)) #True
print(isinstance(m, emp))#True
print(isinstance(e, mgr))#False
print(isinstance(m, mgr))#True

#builtin
print(isinstance("data", str))#True
print(isinstance("data", int)) #False



print(issubclass(emp, emp)) #True
print(issubclass(mgr, emp))#True
print(issubclass(emp, mgr))#False
print(issubclass(mgr, mgr))#True
#-------------------------------------------------



class emp:
    def __init__(self, eno=10,nm="no name"):
        self.empno=eno
        self.ename= nm
        
    def display(self):
        print(f"Employee {self.empno} , {self.ename}")


class mgr(emp):
    pass

e= emp()
m= mgr()
e.display()
m.display()

e= emp(12,"Emp")
m= mgr(15,"mgr")
e.display()
m.display()

#-------------------------------------------------



class emp:
    def __init__(self, eno=10,nm="no name"):
        self.empno=eno
        self.ename= nm
        
    def display(self):
        print(f"Employee {self.empno} , {self.ename}")


class mgr(emp):
    def __init__(self,bns):
        self.bonus=bns
        

e= emp()
m= mgr() #TypeError: mgr.__init__() missing 1 required positional argument: 'bns'
e.display()
m.display()

e= emp(12,"Emp")
m= mgr(1500)
e.display()
m.display()

#-------------------------------------------------



class emp:
    def __init__(self, eno=10,nm="no name"):
        self.empno=eno
        self.ename= nm
        
    def display(self):
        print(f"Employee {self.empno} , {self.ename}")


class mgr(emp):
    def __init__(self,eno,nm,bns):
        super().__init__(eno,nm)
        self.bonus=bns
        



e= emp(12,"Emp")
m= mgr(15,"mgr" ,1500)
e.display()
m.display()


#-------------------------------------------------


#overriding display method
class emp:
    def __init__(self, eno=10,nm="no name"):
        self.empno=eno
        self.ename= nm
        
    def display(self):
        print(f"Employee {self.empno} , {self.ename}")


class mgr(emp):
    def __init__(self,eno,nm,bns):
        super().__init__(eno,nm)
        self.bonus=bns
        
    def display(self):
        super().display()
        print(f"Manager {self.bonus} ")



e= emp(12,"Emp")
m= mgr(15,"mgr" ,1500)
e.display()
m.display()

#-------------------------------------------------
class emp:
    def __init__(self, eno=10,nm="no name"):
        self.empno=eno
        self.ename= nm
        
    def display(self):
        print(f"Employee {self.empno} , {self.ename}")


class mgr(emp):
    def __init__(self,eno,nm,bns):
        super().__init__(eno,nm)
        self.bonus=bns
        
    def display(self):
        super().display()
        print(f"Manager {self.bonus} ")
        
class salesmgr(mgr):
    pass


s= salesmgr(22, "Salesmgr", 8000)
s.display()

#-------------------------------------------------
class A:
    id=100
    
class B:
    id=200
    
class C(A,B):
    id=300
    
    
    
c= C()
print(C.mro()) #[<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>]


print(C.__mro__) #(<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)


#---------------------------------------------

class Testdata:
    def __init__(self):
        self.no=100 #public
        self._no1=200#protected
        self.__no2=300 #private


t= Testdata()
print(t.no)
print(t._no1)
print(t.__no2) #AttributeError: 'Testdata' object has no attribute '__no2'







