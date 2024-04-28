class student:
    def __init__(self):
        self.name="Gaurav"
        self.course="Mca"
        self.roll_no=2311845
        self.marks=300
    def Performance(self):
        self.name=self.name
        self.course=self.course
        self.roll_no=self.roll_no
        self.marks = self.marks-100

s1=student()
print(s1.__dict__)
s1.Performance()
print(s1.__dict__)

        
