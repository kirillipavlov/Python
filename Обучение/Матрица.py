import numpy as np
a = np.array([1,2,3,4] , float)
print(type(a), end = " - тип массива\n")
print(a)
print(a[:2])
print(a[3])
print(a.shape, end = " - размер массива\n")

print("\nдвухмерный массив\n")
a = np.array([[1,2,3,4] , [5,6,7,8]] , float)
print(a)
print(a[0,1])
print(a.shape, end = " - размер массива\n") #размер
print(a.dtype, end = " - тип массива\n") #тип
print(len(a), end = " - длина - количество строк\n") #длина - количество строк
print(2 in a, end = " - вхождение в массив\n")

print()
a = np.array(range(10))
print(a)
l = int(len(a))
print(l)
a = a.reshape((5,2))
print(a)

def prt():
    print(a)
    print(b)
    print(c)
    print()

a = np.array([1,2,3,4] , float)
b = a
c = a.copy()
prt()
a[0] = 9
prt()

a.tolist()
print(a)
print(list(a))

a = np.array([[1,2,3,4] , [5,6,7,8]] , float)
print(a)
print(a.flatten()) #одномерный массив из двухмерного

#объединение массивов
a = np.array([1,2,3,4], float)
b = np.array([1,2,3,], float)
c = np.array([3,4], float)
print(np.concatenate((a,b,c)))

#единичная матрица
print(np.identity(4, dtype = float))
print()
#на k диагонали
print(np.eye(4, k = 1, dtype = float))

#округление
#np.floor(a)
#np.ceil(a)
#np.rint(a)
#print(np.pi)
#print(np.e)