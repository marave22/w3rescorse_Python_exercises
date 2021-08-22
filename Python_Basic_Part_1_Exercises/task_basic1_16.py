# Write a Python program to get the difference between a given number and 17,
# if the number is greater than 17 return double the absolute difference.

number = 17
given_number = int(input("Enter the number: "))

subs = number - given_number
print("This is a difference of the numbers:", subs)
if subs != abs(subs):
    print("Double of the absolute difference:", 2*abs(subs))
else:
    print("This is not a number")
