import datetime as dt

today = dt.date.today()
birth_date = (dt.datetime.strptime(input("What is your birth date? (dd-mm-yyyy) "), "%d-%m-%Y")).date()
age = int((today - birth_date).days / 365)

if today.day == birth_date.day and today.month == birth_date.month:
    print("Happy birthday! You are now " + str(age) + " years old!")
elif age == 0:
    print("Congratulations for the baby! They're not 1 year old yet.")
else:
    print("Age: " + str(age) + " years old.")

input()
