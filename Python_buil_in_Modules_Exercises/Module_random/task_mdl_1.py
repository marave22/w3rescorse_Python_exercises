# Write a Python program to generate a random color hex, a random alphabetical string,
# random value between two integers (inclusive) and a random multiple of 7 between 0 and 70. Use random.randint()

import random
import string

# random color hex
print("Generate a random color hex:", "#{:06x}".format(random.randint(0, 0xFFFFFF)))

# random alphabetical string
max_length = 255
s = ""
for i in range(random.randint(1, max_length)):
    s += random.choice(string.ascii_letters)
print("\nGenerate a random alphabetical string:" + s)

# random value between two integers, inclusive
print("\nGenerate a random value between two integers, inclusive:")
print(random.randint(0, 10))
print(random.randint(-7, 7))
print(random.randint(1, 1))

# random multiple of 7 between 0 and 70
print("\nGenerate a random multiple of 7 between 0 and 70:")
print(random.randint(0, 10) * 7)
