class employee:
    'Class employee having name and age'
    def __init__(self,n,a):
        self.name=n
        self.age=a
    def disp(self):
        print("Name=",self.name,"Age=",self.age)
print("employee.__doc__:",employee.__doc__)
print("employee.__name__:",employee.__name__)
print("employee.__module__:",employee.__module__)
print("employee.__bases__:",employee.__bases__)
print("employee.__dict__:",employee.__dict__)
