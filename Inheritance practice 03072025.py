class Parent1:
    def func(self):
        print("This is an example for Parent class")
    def age(self):
        print("Age is fifty years")

class Child(Parent1):
    def f1(self):
        print("This is an example for Child class")
    def a1(self):
        print("Age is eighteen years")
# p=Parent1()
# p.func()
# p.age()
c=Child()
c.f1()
c.a1()
c.func()
c.age()