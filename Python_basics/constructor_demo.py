# constructor will be called automatically when object of class is created
class Constructor:
    def __init__(self): # constructor
        print("Im constructor")
    
    def method(self): # method
        print("Im method")
    
    def __str__(self): # string representation of object -> toString() of Java
        return "alkesh"
        

obj=Constructor() # constructor is called
obj.method() # calling method
print(obj) # calling toString method
