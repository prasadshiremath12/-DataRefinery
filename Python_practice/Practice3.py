# Super()

class Car:
    def __init__(self, Make, Model, Year):
        self.Make = Make
        self.Model = Model
        self.Year = Year

class car_body_type(Car):
    def __init__(self, Type, Make, Model, Year):
        self.Type = Type
        super().__init__(Make, Model, Year)  # Pass all required arguments at once

C1 = car_body_type("SUV", "Mercedes", "C-Class",2020)
print(C1.Type)
print(C1.Make)
print(C1.Model)
print(C1.Year)