from decimal import Decimal
class Fraction:
    def __init__(self, n):
        self.__first = int(n)
        num = Decimal(str(n - int(n)))
        self.__second = num.quantize(Decimal("1.000"))
    def Sum(self, a, part):
        if part == "1":
            return a + self.__first
        elif part == "2":
            return a + self.__second
        else:
            print("Неверный выбор")
    def Multiply(self, a, part):
        if part == "1":
            return a * self.__first
        elif part == "2":
            return a * self.__second
        else:
            print("Неверный выбор")
n = float(input())
number = Fraction(n)
while True:
    num_ = int(input("Введите число"))
    part = input ("Какую часть использовать (\"end\" для выхода)")
    if part == "end":
        break
    print(number.Sum(num_, part))
    print(number.Multiply(num_, part))