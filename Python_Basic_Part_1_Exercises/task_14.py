# Write a Python program to calculate number of days between two dates.
# Sample dates : (2014, 7, 2), (2014, 7, 11)
# Expected output : 9 days

first_date = list(input("Enter the first date: ").split(', '))
second_date = list(input("Enter the second date: ").split(', '))
num_day = int(first_date[-1]) - int(second_date[-1])

print(abs(num_day), " days")
