class Student:
    branch = "MCA"   # static variable
    def __init__(self,name):
        self.name = name    #instance variable
# for accessing static variable
print(Student.branch)
#for accessing instance variable
obj = Student("Gaurav")
print(obj.name)
