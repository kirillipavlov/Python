alphabet ="abcdefghijklmnopqrstuvwxyz" #26 букв
#text = input("Введите строку: ")
#text = "Hel12o 16e15ple"
text = "Hel12o 16e155ple"
i = 0
s = ""
print(text)
while i < len(text):
    a = text[i]
    while "0" <= a <= "9":
        s += a
        i += 1
        if i < len(text):
            a = text[i]
        else:
            break
    i += 1
    if s != "":
        print(s)
        s = ""
