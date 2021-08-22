# Write a Python program to test whether a number is within 100 of 1000 or 2000.

num = int(input("Please enter the number: "))

while num < 100 or num > 2000:
    print("Enter new number it's not meet with the condition")
    num = int(input("Please enter the number again: "))
    if 100 <= num <= 1000:
        print("Number is within 100 of 1000\n", num)
    elif 1000 < num <= 2000:
        print("Number is within 1000 of 2000\n", num)
