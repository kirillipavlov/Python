print("Введите номер месяца от 1 до 12")
number = int(input())
if number >= 3 and number <= 5:
    print("Весна")
elif number >=6 and number <=8:
    print("Лето")
elif number >=9 and number <=11:
    print("Осень")
elif number >=1 and number <=2:
    print("Зима")
elif number == 12:
    print("Зима")
else:
    print("Вы ввели неверное значение")
