# Write a Python program to accept a filename from the user and print the extension of that.

fileName = input("Enter the file name with extension: ")
fileList = fileName.split(".")
print("The extension of entered file: ", fileList[len(fileList) - 1])
