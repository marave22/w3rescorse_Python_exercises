# Write a Python program to get a string which is n (non-negative integer) copies of a given string.

def larger_string(str1, n):
    result = ""
    for i in range(n):
        result = result + str1
    return result


print(larger_string('abc', 2))
print(larger_string('.py', 3))
print(larger_string('.py', 6))
