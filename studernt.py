class Student:
    
    def __init__(self, stuId):
        self.studentId = stuId
        
    def __str__(self):
        return f"{self.studentId}"

class Employee:
    
    def __init__(self, employeeId, employeeName, employeeSalary):
        self.empId = employeeId
        self.empName = employeeName
        self.empSal = employeeSalary
        
        
    def __str__(self):
        return f"{self.empId} , {self.empName},{self.empSal}"
    

emp1 = Employee(1, "Amit", 10000)
emp2 = Employee(2, "Shyam", 300000)
emp3 = Employee(3,"John", 230000)
stu  = Student(200)
    
empList ={emp1, emp2, emp3, stu}

for em in empList:
    print(em)