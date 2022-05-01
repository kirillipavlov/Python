#Создайте строку от 0 до 10
#Поменяйте местами цифры 5 8
#Выведите на экран два массива: первоначальный и изменённый
#Объедините их
#Сделайте из этой строки 3 столба
import numpy as np
a = np.array(range(11))
b = a.copy() #list(a)
print(a)
b[5], b[8] = b[8], b[5]
print(b)
ab = np.concatenate((a,b))
print(ab)
print()
for i in range(len(ab)):
    print(ab[i], end = "\t")
    if (i+1) % 3 == False:
        print()
print()