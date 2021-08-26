# Write a Python program to get a new string from a given string where "Is" has been added to the front.
# If the given string already begins with "Is" then return the string unchanged.

myStr = input("Please enter the string: ")

if myStr[:2] == "Is":
    print(myStr)
elif myStr[:2] != "Is":
    print("Is " + myStr)
