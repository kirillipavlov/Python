print ("hello")
def decorator(func):
    import time
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(start)
        print(end)
        print ("Время выполнения", end - start)
    return wrapper
@decorator
def webpage():
    import requests
    webpage = requests.get("https://google.com")

#webpage()
from datetime import datetime
#time_ = time()
time_ = datetime.now()
print(time_)