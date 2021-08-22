# Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn. Go to the editor
# Sample value of n is 5
# Expected Result : 615

n = input("Please enter the n number: ")

print("This is the result", (int(n) + int(n+n) + int(n+n+n)))
