class Organisation:
    emp_id = 1001
    org_name = "TATA"
    Tot_emp = 0
    def __init__(self,name,department,designation):
        self.id = Organisation.emp_id
        Organisation.emp_id += 1
        self.organisation = Organisation.org_name
        Organisation.Tot_emp += 1 
        self.name = name
        self.department = department
        self.designation = designation
    def emp_information(self):
        print("Id", self.id)
        print("Organisation Name is :", self.organisation)
        print("Name of employee is :", self.name)
        print("Department :", self.department)
        print("Designation of employee is :", self.designation)
        print("Total number of employee is :", Organisation.Tot_emp)
emp1 = Organisation("Gaurav", "MCA", "Student")
emp1.emp_information()
emp2 = Organisation("Divyanshu", "MCA", "Student")
emp2.emp_information()
emp3 = Organisation("Yash", "MCA", "Student")
emp3.emp_information()
emp4 = Organisation("Prateek", "MCA", "Student")
emp4.emp_information()
