print ("Введите ваше имя:", end = " ")
name = input()
with open("hi.txt", "w") as sfile:
    sfile.write("Здравствуйте, " + name)
    sfile.write("\nВаше направление в обучении: Python-разработчик")
    print("файл создан")

print("\nЧтение полностью\n")
with open("hi.txt", "r") as sfile:
    print(sfile.read())

print("\nЧтение по строчно\n")
with open("hi.txt", "r") as sfile:
    for i in sfile:
        print(i, end = "")
        
print("\nЧтение в список\n")
with open("hi.txt", "r") as sfile:
    content = sfile.readlines()
    print(content)
    print()
    for i in range(len(content)):
        print(content[i], end = "")

print("\n***Программа завершена")
#print(name)