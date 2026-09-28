class Employee:
    def __init__(self, Role, Department, Salary):
        self.Role = Role
        self.Department = Department
        self.Salary = Salary

    def ShowDetails(self):
        print("Role:", self.Role)
        print("Department:", self.Department)
        print("Salary:", self.Salary)

class Engineer(Employee):
    def __init__(self, Name, Age):
        self.Name = Name
        self.Age = Age
        super().__init__("Engineer", "IT", 233)
        # super().__init__(self.Role, self.Department, self.Salary)

    def ShowDetails1(self):
        print(self.Name, self.Age)

# E1= Employee('Data engineer', "Data Science", 100000)
E1=Engineer("Prasad", 26)
E1.ShowDetails()
E1.ShowDetails1()


