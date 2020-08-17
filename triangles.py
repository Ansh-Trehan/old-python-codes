a=int(input("please enter the first side"))
b=int(input("please enter the second side"))
c=int(input("please enter the third side"))
if (a==b==c):
    print("the traingle is equilateral")
elif ((a==b!=c) or (b==c!=a) or (a==c!=b)):
    print("the triangle is isoscles")
else:
    print("the triangle is a scalar triangle")
