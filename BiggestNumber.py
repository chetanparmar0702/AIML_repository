num1 = int(input("Enter the number"))
num2 = int(input("Enter the number"))
num3 = int(input("Enter the number"))
max1 = 0


def biggest_num(num1, num2, num3):
    if (num1 > num2 and num1 > num3):
        max1 = num1
    elif (num2 > num3):
        max1 = num2
    else:
        max1 = num3
    print("The biggest number is: ", max1)


biggest_num(num1, num2, num3)
