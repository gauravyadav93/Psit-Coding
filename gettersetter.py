class student:
    def __init__(self,id1,name):
        self.__id1 = id1
        self.name = name
    def get_id1(self):
        return self.__id1
    def set_id1(self,id1):
        self.__id1=id1
    def get_name(self):
        return self.name
    def set_name(self,name):
        self.name = name
stu_obj = student(101,"Jenny")
print(stu_obj.get_id1())
print(stu_obj.get_name())
stu_obj.set_id1(102)
stu_obj.set_name("Jennifer")
print(stu_obj.get_id1())
print(stu_obj.get_name())





