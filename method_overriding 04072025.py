class A:
    def function_one(self):
        print('class A function one')
    def function_two(self):
        print('class A funtion two')
class B(A):
    def fucntion_two(self):
        print('class B funtion two')
    def function_three(self):
        print('class B function three')
one=B()
one.function_one()
one.function_two()
one.function_three()

