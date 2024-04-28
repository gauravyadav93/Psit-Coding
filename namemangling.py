class A:
    def __init__(self,a,b):
        self.a=a
        self.__b=b
    def display(self):
        print(self.__b)
t1 = A(2,3)
print(t1.a)
t1.display()
print(t1._A__b)
