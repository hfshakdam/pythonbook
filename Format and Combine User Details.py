import datetime

current_year = datetime.datetime.now().year
first_name = "Hisham"
last_name = "Vermine"
yob = 2001
age = current_year - yob
print(f"Hello {first_name} {last_name}, you are {age}")