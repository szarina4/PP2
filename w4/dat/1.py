from datetime import datetime,timedelta
day1=int(input("Enter the day: "))
mon1=int(input("Enter the month: "))
year1=int(input("Enter the year: "))
a=datetime(year1,mon1,day1)
day5before=a-timedelta(days=5)
print(day5before)

