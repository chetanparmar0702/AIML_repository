# x=int(input('enter a number'))
# def even_odd():
#     if (x%2==0):
#         print('even')
#     else:
#         print('odd')
# even_odd()

temp_type=input("Are you entering the temperature in celcius")
temp= float (input("Enter the temperature:"))
conv_temp = 0
def temp_convertion(temp_type,temp):
    print(temp_type)
    if(temp_type == "celcius"):
        conv_temp = (temp*9/5)+32
    else:
        conv_temp = (temp-32)*5/9
    return conv_temp

c= temp_convertion(temp_type,temp)
print(c)
#
# A=[10,20,30,40,50]
# total=0
# for item in A:
#         total= total+item
# print(total)
#
# y=[10,20,60,100]
#
# def find_max():
#     if (y>=100):
#         print('larget number')
#     else:
#         print('small number')
# find_max()

# username = input("enter username")
# password= input(" enter password")
# def login():
#         if (username=='admin' and password=='password123'):
#             print('login successfull')
#         else:
#             print('login unsuccessful')
# login()

# x=[pune,mumbai,bangalore,delhi,chennai]
# for i in range(4,-1,-1):
#     print (x[i])
