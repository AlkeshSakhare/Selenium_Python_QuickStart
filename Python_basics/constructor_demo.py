# constructor will be called automatically when object of class is created
class Constructor:
    def __init__(self): # constructor
        print("Im constructor")
    
    def method(self):
        print("Im method")

obj=Constructor() # constructor is called
obj.method()
