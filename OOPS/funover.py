#case:1 function overloading
#python does'nt support function overloading that's why it only
#executes only the last function

class fn_over:
    def display(self,a):
        print("first function")
    def display(self,a,b):
        print("second function")
obj = fn_over()
obj.display(3,6)

#case: 2 Python supports concept of method overriding

class fn_over:
    def display(self,a):
        print("super class method")
class sub(fn_over):
    def display(self):
        print("sub class method")
    
s1 = sub()
s1.display()
s2 = fn_over()
s2.display(5)

