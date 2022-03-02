from datetime import datetime,timedelta
today=datetime.now()
yester=today-timedelta(days=1)
tomor=today+timedelta(days=1)
print("Today is ",today)
print("Yesterday was",yester)
print("Tomorrow will be  ",tomor)

