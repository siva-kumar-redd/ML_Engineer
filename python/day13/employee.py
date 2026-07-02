class Employee:
    def employee_details(self,employee_id,name,salary):
        self.employee_id = employee_id
        self.name = name
        self.salary = salary

emp1 = Employee()
emp2 = Employee()


emp1.employee_details(1,"Kiran",25000)
emp2.employee_details(2,"sunil",35000)
print(emp1.employee_id,emp1.name,emp1.salary)
print(emp2.employee_id,emp2.name,emp2.salary)
