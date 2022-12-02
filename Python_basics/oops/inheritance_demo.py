# python support 4 types of inheritance
# single: single parent and child
# multiple: multiple parent for single child
# Hierarchy : multiple child for single parent)
# multilevel inheritance : parent will have child and grand child

# Single level : Parent -> Child

class Parent:
    p = 10

    def methodOfParent(self):
        print("Im Parent method having variable p = ", self.p)


class Child(Parent):  # inheriting class Child extends Parent
    c = 20

    def methodOfChild(self):
        print("Im Child method having variable c = ", self.c)


c = Child()
c.methodOfChild()
c.methodOfParent()
