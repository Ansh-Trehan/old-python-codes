class employee:
    def __init__(self, n, s):
        self.name=n
        self.salary=s
    def disp(self):
        print("Name = ", self.name)
        print("Salary = ", self.salary)
emp1=employee("Ansh", 2000)
print(hasattr(emp1, "name"))
print(hasattr(emp1, "age"))
print(getattr(emp1, "name"))
#print(getattr(emp1, "age"))
setattr(emp1, "name", "Ansh Trehan")
emp1.disp()
delattr(emp1, "salary")
print(emp1.name)
#print(emp1.salary)
