class Example:
    def __init__(self):
        print ("Object created")
    def __del__(self):
        print ("Object destroyed")
myObj = Example()
del myObj
