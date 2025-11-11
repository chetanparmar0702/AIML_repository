class Calc:
    def add(self):
        print('add')

    def sub(self):
        print('substraction')
    def mul(self):
        print('multiplication')
    def div(self):
        print('division')
one=Calc()
one.add()
one.sub()
one.mul()
one.div()

class SciCalc(Calc):
    def sin(self):
        print()
    def cos(self):
        print()
one=SciCalc()
one.sin()
one.cos()
one.add()
one.sub()
one.mul()
one.div()