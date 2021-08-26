# Write a Python program to count the number of characters (character frequency) in a string.

myStr = input("Pleas enter the string: ")
myDict = {}

for i in myStr:
    keys = myDict.keys()
    if i in keys:
        myDict[i] += 1
    else:
        myDict[i] = 1

print(myDict)
