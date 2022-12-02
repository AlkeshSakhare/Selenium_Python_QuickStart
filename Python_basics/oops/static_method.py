# Non static -> can be called by object only
# Static -> can be called by class name
class A:
    def nonstatic(self):
        print("Im nonstatic method")

    @staticmethod
    def staticMethod():
        print("Im static method")


A.staticMethod()  # called by class name
A().nonstatic()  # called by object of class
