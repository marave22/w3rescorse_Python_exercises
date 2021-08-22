# Write a Python program to calculate the sum of three given numbers,
# if the values are equal then return three times of their sum.

num1 = int(input("Please enter the first number: "))
num2 = int(input("Please enter the second number: "))
num3 = int(input("Please enter the third number: "))

if num1 == num2 == num3:
    sum_3 = (num1 + num2 + num3) * 3
    print("This is the sum of equal numbers with three times: ", sum_3)
else:
    sum_3 = num1 + num2 + num3
    print("The sum of not equal numbers: ", sum_3)
