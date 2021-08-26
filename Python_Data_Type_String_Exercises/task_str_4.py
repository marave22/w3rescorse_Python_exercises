# Write a Python program to get a string from a given string where all occurrences of its first char
# have been changed to '$', except the first char itself. Go to the editor
# Sample String : 'restart'
# Expected Result : 'resta$t'

def change_string(my_str):
    char1 = my_str[0]
    my_str = my_str.replace(char1, '$')
    my_str = char1 + my_str[1:]
    print(my_str)

    return my_str


change_string("sdfg")
