# class Calc:
#     def add(self):
#         print('add')
#
#     def sub(self):
#         print('substraction')
#     def mul(self):
#         print('multiplication')
#     def div(self):
#         print('division')
#     one= Cacl()
#     one.add()
#     one.sub()
#     one.mul()
#     one.div()
#
# class SciCalc(Calc):
#     def sin(self):
#         print()
#     def cos(self):
#         print()
#     one=SciCalc()
#     one.sin()
#     one.cos()
#     one.add()
#     one.sub()
#     one.mul()
#     one.div()


class Parent1:
    def func(self):
        print("This is an example for Parent class")
    def age(self):
        print("Age is fifty years")

class Child:
    def f1(self):
        print("This is an example for Child class")
    def a1(self):
        print("Age is eighteen years")
p=Parent1()
p.func()
p.age()
c=Child()
c.f1()
c.a1()





