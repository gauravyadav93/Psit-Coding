#example of encapsulation
class Student:
    def __init__(self,rollno,name):
        self.__rollno = rollno           #private attribute/instance
        self.name = name    # public attribute
    def display(self):
        print(self.__rollno)
        print(self.name)
stu_obj1 = Student(23,"Jenny")
stu_obj1.display()
#print(stu_obj1.__rollno)  # it will give an error because it
#is private member can be accessed only inside the class
print(stu_obj1.name)    # it is an public member        
