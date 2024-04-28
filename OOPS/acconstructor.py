#Accessing constructor from subclass
#case1: if sub class dont have constructor

'''class Area:
    def __init__(self,len1,br):
        self.len1 = len1
        self.br = br
class cal_Area_tri(Area):
    def Tri_Area(self):
        area=0.5*self.len1*self.br
        print("Area of tri:", area)
obj = cal_Area_tri(4,6)
obj.Tri_Area()'''

#case2: if both the classes have constructor

class Area:
    def __init__(self,len1,br):
        self.len1 = len1
        self.br = br
class cal_Area_tri(Area):
    def __init__(self):
        super().__init__(5,6) #first method of using constructor of parent class
        Area.__init__(self,5,6) #second method of using constructor of parent class
    def Tri_Area(self):
        area=0.5*self.len1*self.br
        print("Area of tri:", area)
obj = cal_Area_tri()
obj.Tri_Area()


