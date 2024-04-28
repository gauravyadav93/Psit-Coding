#Multiple Inheritance
class Calculation1:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def Summation(self,a,b):
        return a+b;
class Calculation2:
    def __init__(self,a,b):
        super().__init__(a,b)
    def Multiplication(self,a,b):
        return a*b;
class Derived(Calculation1,Calculation2):
    def __init__(self,a,b):
        super().__init__(a,b)
    def Divide(self,a,b):
        return a/b;
d = Derived(10,20)
print(d.Summation(10,20))
print(d.Multiplication(10,20))
print(d.Divide(10,20))
