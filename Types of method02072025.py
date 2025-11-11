# class Typemethod:
#     def __init__(self):
#         print('init method')
#     def instance(self):
#         print('instance method')
#     @classmethod
#     def class_method(cls):
#             print('class method')
#     @staticmethod
#     def static_method():
#             print('static method')
# t=Typemethod()
# t.instance()
# Typemethod.class_method()
# Typemethod.static_method()

# class AssignmentMethods:
#     def __init__(self,x,y):
#         print(x)
#         print(y)
#     def sample(self,name):
#         print(name)
#     @classmethod
#     def sample_two(cls,a,b,c):
#         print(a+b+c)
#     @staticmethod
#     def sample_three(x):
#         print(x)
# a=AssignmentMethods(10,20)
# a.sample('chetan')
# AssignmentMethods.sample_two(10,30,40)
# AssignmentMethods.sample_three(500)

class Assignment:
    x=10
    y=20
    def method_one(self,x):
        self.z=30
        print(self.z)

    @classmethod
    def method_two(cls,y):
        print(y)
print(Assignment.x)
print(Assignment.y)
a=Assignment()
a.method_one(20)
Assignment.method_two(30)

# class Test:
#     print('class')
# test_one=Test()
# tets_two=Test()
