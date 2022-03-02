from datetime import datetime
print("The format must be 2012-05-29 15:00:23")
a=input("Enter the 1st date: ")
b=input("Enter the 2st date: ")
date1=datetime.strptime(a,'%Y-%m-%d %H:%M:%S')
date2=datetime.strptime(b,'%Y-%m-%d %H:%M:%S')
diff=date1-date2
print(diff.days*3600*24+diff.seconds)
