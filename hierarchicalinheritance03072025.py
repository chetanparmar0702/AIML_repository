class A:
    def func(self):
        x=10
        print(x)
class B(A):
    def f1(self):
        y=20
        print(y)
class C(A):
    def f2(self):
        z=30
        print(z)
a=C()
b=B()
a.func()
b.f1()
a.f2()


