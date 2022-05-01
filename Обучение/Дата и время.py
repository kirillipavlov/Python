print ("hello")
import datetime
yesterday = datetime.date(2018, 3, 2)
today = datetime.date.today()
print(today)
print()

from datetime import date
today = date.today()
print(today)
print(today.day)
print(today.month)
print(today.year)

print("Время")
from datetime import time
time_ = time()
print(time_)
time_ = time(15,0,20)
print(time_)

print()
from datetime import datetime
date_ = datetime(2018,3,2)
date_ = datetime.now()
print(date_)

#strptime(str, format)
#%d %m %y %Y %H %M %S
from datetime import datetime
date_ = datetime.strptime("12/2/2019", "%d/%m/%Y")
print(date_)
date_ = datetime.strptime("12/2/2019", "%m/%d/%Y")
print(date_)

print()
import locale
locale.setlocale(locale.LC_ALL, "")
now = datetime.now()
print(now)
print(now.strftime("%d %m %Y %A"))

#timedelta(дни, секунды, миллисекунды, минуты, часы, недели)
print()
from datetime import timedelta, datetime
date = timedelta(hours = 4)
print(date)
date = timedelta(4)
print(date)
print()
now = datetime.now()
print(now)
two_days = timedelta(2)
print(now + two_days)
print(now + timedelta(hours = 10))