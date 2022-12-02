# Example 1:
class overloading:
    def callme(self, name=None):
        if name is not None:
            print("Hello ", name)
        else:
            print("Hello")


o1 = overloading()
o1.callme()
o1.callme("Alkesh")


# Example 2:

class sum:
    def addme(self, a=0, b=0, c=0):
        print(a+b+c)


s = sum()
s.addme(20, 30)
s.addme(20, 30, 40)
