# Write a Python program which accepts a sequence of comma-separated numbers
# from user and generate a list and a tuple with those numbers.

numbers = input("Please enter the comma-separated numbers: ")
listNumbers = numbers.split(", ")
tupleNumbers = tuple(numbers.split(", "))
print("List: ", listNumbers)
print("Tuple: ", tupleNumbers)
