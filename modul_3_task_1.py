from datetime import datetime


def get_days_from_today(date):
    try:
        today = datetime.today().date()
        date = datetime.strptime(date, "%Y-%m-%d").date()
        diff_day = (today - date).days
        return diff_day
    except ValueError:
        return print("You entered an invalid date format")

user_date = input("Enter your date(YYYY-MM-DD): ")
diff_days = get_days_from_today(user_date)
if diff_days is not None:
    print(f"Days between dates:{diff_days}")
