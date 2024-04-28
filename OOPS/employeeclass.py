class Employee:
    def __init__(self,id1,name,designation,department,bsal):
        self.id1 = id1
        self.name = name
        self.designation = designation
        self.department = department
        self.basicsalary = bsal
        self.hra = 0
        self.va = 0
        self.netsalary = 0
    def Cal_hra_va_basic(self):
        self.hra = 0.3*self.basicsalary
        self.va = 0.2*self.basicsalary
        self.netsalary = self.hra + self.va + self.basicsalary
    def display(self):
        print("id = ",self.id1)
        print("Name = ",self.name)
        print("Designation = ",self.designation)
        print("Department = ",self.department)
        print("Hra = ",self.hra)
        print("va = ",self.va)
        print("Net Salary = ",self.netsalary)
emp_obj1 = Employee("G12","Gaurav","Developer","IT",50000)
emp_obj2 = Employee("D23","Divyanshu","Web Developer","IT",70000)
emp_obj2.Cal_hra_va_basic()
emp_obj2.display()
emp_obj1.Cal_hra_va_basic()
emp_obj1.display()
#print(emp_obj1.__dict__)
        
