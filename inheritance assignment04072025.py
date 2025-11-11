class A:
    def function_one(self):
        print('class-A function')
class B(A):
    def function_two(self):
        print('class-B function')
class C(B):
    def function_three(self):
        print('class-C function')
c1=C()
c1.function_one()
c1.function_two()
c1.function_three()


