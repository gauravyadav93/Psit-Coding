#Example of static variable
class Student:
    clg = "psit"
    def __init__(self,name,roll_no):
        self.name = name
        self.roll_no = roll_no
    def print_Detail(self):
        print("name = ",self.name)
        print("Roll No. = ",self.roll_no)
        print("college = ", Student.clg)
obj1 = Student("raj",123)
obj1.print_Detail()
obj2 = Student("geny",124)
obj2.print_Detail()
obj3 = Student("Shikha",125)
