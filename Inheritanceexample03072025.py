class School:
    def atten(self):
        print('attendance is full')
    def add(self):
        print('address is pune')
class Student(School):
    m1=0
    m2=0
    m3=0
    t=0
    def details(self):
        name=input('enter a name')
        rollNo=input('enter rollNo')
        self.m1=int(input('enter mark1'))
        self.m2=int(input('enter mark2'))
        self.m3=int(input('enter mark3'))
    def total_display(self):
        self.t=self.m1+self.m2+self.m3
        print(self.t)
    def percentage(self):
        percentage=self.t/3
        print(percentage)
class Gender(Student):
    def boys(self):
        count=int(input('enter number'))
    def girls(self):
        count=int(input('enter number'))
class Teacher(School):
    def salary(self):
        calculation=int(input('enter a number'))
    def classes(self):
        classes= int(input('enter a number'))

t=Teacher()
t.atten()
t.add()
t.salary()
t.classes()
g=Gender()
g.details()
g.total_display()
g.percentage()
g.boys()
g.girls()

