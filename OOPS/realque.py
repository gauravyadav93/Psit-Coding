class Bank:
    def __init__(self):
        self.roi = "ROI:-"
    def getRateOfInterest(self):
        print(self.roi)
class SBI(Bank):
    def __init__(self):
        self.roi = "8%"
    def getRateOfInterest(self):
        print(self.roi)
class ICICI(Bank):
    def __init__(self):
        self.roi = "7%"
    def getRateOfInterest(self):
        print(self.roi)
class AXIS(Bank):
    def __init__(self):
        self.roi = "9%"
    def getRateOfInterest(self):
        print(self.roi)
objp = Bank()
objp.getRateOfInterest()
obj1 = SBI()
obj1.getRateOfInterest()
obj2 = ICICI()
obj2.getRateOfInterest()
obj3 = AXIS()
obj3.getRateOfInterest()
    
        
        
        
