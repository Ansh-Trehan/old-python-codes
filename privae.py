class employee:
    def __init__(self,n,s,a):
        self.name=n
        self.salary=s
        self.__age=a
    def disp(self):
        print("Name = ", self.name)
        print("Salary = ",self.salary)
        print("Age = ",self.__age)

emp1=employee("Ansh",2000,35)
emp1.disp()
print(emp1.name)
print(emp1.salary)
print(emp1._employee__age)
#print(emp1.__age)
