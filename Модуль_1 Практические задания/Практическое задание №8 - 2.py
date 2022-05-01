print("Введите строку")
string = input()
#string = "Hello, ToM. I aM haPPy."
count = 0
for i in range(0,len(string)):
    if string[i].isupper() == True:
        count += 1
print("Количество заглавных букв:", count)
