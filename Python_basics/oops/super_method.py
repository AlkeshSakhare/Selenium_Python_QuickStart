# super() is used to call parent method/ variable
class A:
    var = 20

    def a(self):
        print("parent class")


class B(A):
    def b(self):
        super().a()  # parent a() is called
        print("Parent var: ", super().var)
        print("child class")


b = B()
b.b()
