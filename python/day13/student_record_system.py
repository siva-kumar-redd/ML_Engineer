class Student:
    def __init__(self,name,roll_number,branch,cgpa):
        self.name = name
        self.roll_number = roll_number
        self.branch = branch
        self.cgpa = cgpa
    
    def display(self):
        print("Name:",self.name)
        print("roll_number:",self.roll_number)
        print("branch:",self.branch)
        print("cgpa:",self.cgpa)
stu1 = Student("Siva",25,"CSE",8.5)
stu2 = Student("Kiran",28,"CSE",9.5)
stu3 = Student("Venky",24,"Stats",9.5)

stu1.display()
stu2.display()
stu3.display()