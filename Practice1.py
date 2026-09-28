class Student:
    School="Little Scholars Academy"
    def __init__(self, Name, Age, Gender, Address, Government_identity):
        self.Name = Name
        self.Age = Age
        self.Gender = Gender
        self.Address = Address
        self.Government_identity = Government_identity

    def Check_student_details(self):
        print(self.Name, self.Age, self.Gender, self.Address, self.Government_identity)

    @staticmethod
    def hello():
        print("Hello")

    def Examination(self, Marks):
        self.Marks = Marks
        sum=0
        for mark in Marks:
            sum += mark
        i=0
        for i in Marks:
            i+=1
        percentage= sum/i
        print(str(percentage)+'%', "percentage")

S1= Student("Prasad", 26, "Male", "Shreenagar, Belagavi-590016", 452853823626)

S1.Examination([100,46,26,66,99])
S1.Name="Karthik"
S1.Check_student_details()
S1.hello()