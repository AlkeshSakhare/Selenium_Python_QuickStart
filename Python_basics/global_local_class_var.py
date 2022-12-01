# methods - can be access in any class
# function - can be access in same python file

# methods takes 1 argugment as self which means class

# local variale can be access directly
# instance variable can be access by self.variable_name
# global variable can be access by globals[].('variable_name')



a,b=10,20 # global variables

class variables:
    a,b=30,40 # instance variables

    def var(self,a,b):
        print("Im local variable: a", a)
        print("Im local variable: a", b)
        print("Im instance variable: a", self.a)
        print("Im instance variable: a", self.b)
        print("Im global variable: a", globals()['a'])
        print("Im global variable: a", globals()['b'])

var=variables()
var.var(50,60)