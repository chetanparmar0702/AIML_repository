class A:
    def __init__(self):
        print('class A constructor')
class B(A):
    def __init__(self):
        print('class B constructor')
class C(B):
    def __init__(self):
        print('class C constructor')
obc=C()

class X:
    def __init__(self):
        print('class A constructor')
class Y(X):
    pass
class Z(Y):
    pass

obj=Z()

#super()
class A:
    def __init__(self):
        print('class A constructor')
class B(A):
    def __init__(self,X):
        super().__init__()
        print('class B constructor',X)
class C(B):
    def __init__(self):
        super().__init__(100)
        print('class C constructor')

obj=C()
