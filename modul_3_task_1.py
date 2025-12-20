from datetime import datetime


def get_days_from_today(date):
    today = datetime.today().date()
    date = datetime.strptime(date, "%Y-%m-%d").date()
    diff_day = (today - date).days 
    return print(f"The difference between the entered date: {date} and today: {today} is {diff_day} days")

user_date = input("Enter your date(YYYY-MM-DD): ")
try:
    diff_days = get_days_from_today(user_date)
    
except ValueError:
    print(f"You entered an invalid date format: {user_date}.")