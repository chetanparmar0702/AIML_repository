# class A:
#     x=10
# class B(A):
#     y=20
class A:
    def func(self):
        x=10
        print(x)
class B(A):
    def f1(self):
        y=20
        print(y)
class C(B):
    def f2(self):
        z=30
        print(z)
a=C()
a.func()
a.f1()
a.f2()
