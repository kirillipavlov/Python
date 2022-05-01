import random
#x = random.random()
print(random.random())
print(random.random() * 1000)
print(random.randint(10,20))
#randrange(stop)
#randrange(start,stop)
#randrange(start,stop,step)
print(random.randrange(100))
print("****************")
numbers = [1,2,3,4,5,6,7,8,9]
print(random.choice(numbers)) #случайное число
random.shuffle(numbers) #перемешивание
print(numbers)