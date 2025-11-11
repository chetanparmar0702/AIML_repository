# print('Hello')
# try:
#     li=[1,2,3,4,5]
#     print(li[9])
# except Exception as e:
#     print(e)
# try:
#     print(10/0)
# except Exception as e:
#     print(e)
#
# print('Bye')

try:
    x=int(input(' enter a number'))
    print(x)
    y=[10,20,30]
    print(y[0])
    print(y[1])
    print(y[2])
    print(y[3])
except ValueError:
    print('enter a valid number')
except NameError:
    print('x is valid')
except IndexError:
    print('you are accessing wrong position')
