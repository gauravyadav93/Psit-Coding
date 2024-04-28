#Multilevel Inheritance

class Grandfather:
    def __init__(self):
        self.name = "Charu Dixit"
        self.nickname="chia"
    def f1(self):
        print("base class method")
class Father(Grandfather):
    def __init__(self):
        #pass
        super().__init__()
    def f2(self):
        print("first sub class method")
class child(Father):
    def f3(self):
        print("second sub class method")
class child1(child):
    def f4(self):
        print("third sub class method")
obj = child1()
obj.f1()
obj.f2()
obj.f3()
obj.f4()
print(obj.name)
print(obj.nickname)
