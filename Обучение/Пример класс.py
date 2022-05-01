print ("hello")
class Rec:
    def __init__(self, a, b):
        self.__a = a
        self.__b = b
        self.__S = self.__a * self.__b
        self.__P = (self.__a + self.__b) * 2
    @property
    def S(self):
        return self.__S
    @property
    def P(self):
        return self.__P

a = int(input())
b = int(input())
obj = Rec(a,b)

print(obj.P, obj.S)
