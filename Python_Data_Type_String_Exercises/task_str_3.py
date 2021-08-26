# Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string.
# If the string length is less than 2, return instead of the empty string.
# Sample String : 'w3resource'
# Expected Result : 'w3ce'
# Sample String : 'w3'
# Expected Result : 'w3w3'
# Sample String : ' w'
# Expected Result : Empty String

# my_str = input("Please enter the string: ")

def string_length(my_str):
    new_str = ""
    # print(len(my_str))
    # print(my_str[1:])
    # print(my_str[0])
    if len(my_str) < 2:
        print("The string length is less than 2: Empty String", new_str)
    else:
        new_str = my_str[0:2] + my_str[-2:]
        print(new_str)
    return new_str


string_length("Ml")
