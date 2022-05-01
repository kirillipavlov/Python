#Требуется создать словарь, который в качестве ключей будет принимать данные числа
#(т. е. ключи будут типом int), а в качестве значений – количество этих чисел в имеющейся
#последовательности.
#Для построения словаря создайте функцию count_it(sequence), принимающую строку из цифр.
#Функция должна возвратить словарь из 3-х самых часто встречаемых чисел.
#Дана строка в виде случайной последовательности чисел от 0 до 9.
#Итог {2 :  5, 5 : 3, 9 : 4}
import copy
s = "2122234555768290909389"
#s = "5455"
def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k
def count_it(sequence):
    a = {int(x) : sequence.count(x) for x in sequence}
    a2 = copy.deepcopy(a)
    a_out = {}
    if len(a) >= 3:
        for i in range(3):
            max_value = max(a2.values())
            temp = {k: v for k, v in a2.items() if v == max_value}
            k = get_key(a2, max_value)
            a2.pop(k)
            a_out.update(temp)
    else:
        a_out = a2
    print(a)
    print()
    print(a_out)
print(s)
count_it(s)
