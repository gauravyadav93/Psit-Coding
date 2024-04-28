class marks:
    def __init__(self,s1,s2,s3,s4,s5):
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
        self.s4 = s4
        self.s5 = s5
    def percentage(self):
        per = ((self.s1 + self.s2 + self.s3 + self.s4 + self.s5)*100)/500
        
        if(per>=60 and per<=75):
            print("First Division")
        elif(per>=50 and per<=60):
            print("Second Division")
        elif(per>=40 and per<=50):
            print("Third Division")
        elif(per<40):
            print("Failed")
        else:
            print("Honors")
m1 = int(input("Enter Marks of English"))
m2 = int(input("Enter Marks of hindi"))
m3 = int(input("Enter Marks of science"))
m4 = int(input("Enter Marks of maths"))
m5 = int(input("Enter Marks of sanskrit"))

obj = marks(m1,m2,m3,m4,m5)
obj.percentage()
        
        
        
        
        
        
