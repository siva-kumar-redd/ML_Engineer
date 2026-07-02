class Student:
    def __init__(self,employee_id,name,department,salary):
        self.employee_id = employee_id
        self.name = name
        self.department = department
        self.salary = salary
    
    def display(self):
        print("Employee ID:",self.employee_id)
        print("name:",self.name)
        print("department:",self.department)
        print("salary:",self.salary)
stu1 = Student(25,"Siva","CSE",80000)
stu2 = Student(22,"Kiran","CSE",90000)
stu3 = Student(27,"Swetha","AI",75000)

employees = [stu1,stu2,stu3]
count=0
for i in employees:
    if i.salary>50000:
        count+=1
print("no of employees",count)
stu1.display()
stu2.display()
stu3.display()