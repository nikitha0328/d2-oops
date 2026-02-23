class Student:
    
    college_name = "ABC College"

    
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    
    @classmethod
    def change_college(cls, new_name):
        cls.college_name = new_name

    
    @staticmethod
    def is_pass(marks):
        return "Pass" if marks >= 35 else "Fail"

   
    def display(self):
        print("Name:", self.name)
        print("Roll No:", self.roll_no)
        print("College:", Student.college_name)
        print("-------------------")



s1 = Student("Rahul", 101)
s2 = Student("Anita", 102)

s1.display()
s2.display()


Student.change_college("XYZ College")

print("After changing college name:\n")


s1.display()
s2.display()

print("Result:", Student.is_pass(80))
print("Result:", Student.is_pass(20))
