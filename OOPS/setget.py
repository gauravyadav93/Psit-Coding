class student:
    def __init__(self,n):
        self.name = n
    def get_name(self):
        return self.name
    def set_name(self,name):
        self.name = name
obj_stud = student("Divya")
print(obj_stud.get_name())
obj_stud.set_name("Ram Pyari")
print(obj_stud.get_name())
