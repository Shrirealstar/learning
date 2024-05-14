import datetime
today = datetime.date.today()
currect_year = datetime.date.today().year
n = int(input("Enter your year of birth : "))
age = currect_year - n
if age > 60:
    print("You are senior citizen")
else :
    print("You are not senior citizen")
