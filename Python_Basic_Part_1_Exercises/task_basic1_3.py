# Write a Python program to display the current date and time.

import datetime
from datetime import date
today = date.today()
now = datetime.datetime.now()
print("Today's date: ", today, now.strftime("%Y-%m-%d %H:%M:%S"))
