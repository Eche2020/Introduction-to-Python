# Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created
class Emmanuel:
    def __init__(self, age, sex):
        self.age = age
        self.sex = sex

p1 = Emmanuel(50, "male")

print(p1.age, p1.sex)
