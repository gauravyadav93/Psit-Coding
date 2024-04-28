#Hierarichal Inheritance

class Area:
    def __init__(self,l,b,r):
        self.len = l
        self.br = b
        self.r = r
    def display(self):
        print(self.len)
        print(self.br)
class AreaCircle(Area):
    def __init__(self,a,b,r):
        super().__init__(a,b,r)
    def calarea_circle(self):
        print(3.14*self.r*self.r)
class AreaTriangle(Area):
    def __init__(self,a,b,r):
        super().__init__(a,b,r)
    def calAreaTri(self):
        print(0.5*self.len*self.br)
obj1 = AreaCircle(2,4,6)
obj2 = AreaTriangle(3,4,6)
obj1.calarea_circle()
obj2.calAreaTri()
