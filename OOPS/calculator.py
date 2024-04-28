class Calculator:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def add(self):
        res=self.num1+self.num2
        print(res)
    def sub(self):
        res1=self.num1-self.num2
        print(res1)
    def mul(self):
        res2=self.num1*self.num2
        print(res2)
    def div(self):
        res3=self.num1/self.num2
        print(res3)
    def remainder(self):
        res4=self.num1%self.num2
        print(res4)
    def floor(self):
        res5=self.num1//self.num2
        print(res5)
num1=int(input("enter num1:"))
num2=int(input("enter num2:"))
calculatorobj=Calculator(num1,num2)
calculatorobj.add()
calculatorobj.sub()
calculatorobj.mul()
calculatorobj.div()
calculatorobj.remainder()
calculatorobj.floor()
    

    
