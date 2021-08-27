# Write a Python program to get a single string from two given strings, separated by a space and
# swap the first two characters of each string.

def single_string(str1, str2):
    str1_1, str2_1 = "", ""
    if len(str1) == len(str2):

        str1_list = list(str1)
        str2_list = list(str2)
        x = str1_list[0]
        str1_list[0] = str2_list[0]
        str2_list[0] = x
        str1_1 = "".join(str1_list)
        str2_1 = "".join(str2_list)
        print(str1_1, str2_1)
    else:
        print("The strings doesn't have same space")
    return str1_1, str2_1


single_string("sss", "abc")
