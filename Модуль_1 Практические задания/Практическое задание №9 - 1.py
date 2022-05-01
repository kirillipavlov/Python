alphabet ="abcdefghijklmnopqrstuvwxyz" #26 букв
text = input("Введите строку: ")
#text = "Hel12o 16e15ple"
#text = "Hel12o 16e155ple"
i = 0
s = ""
#print(text)
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
        #проверка что бы число было в диапазоне количества букв в алфавите
        if int(s) > len(alphabet):
            s2 = int(s) % len(alphabet) #если число больше количества букв в алфавите, проходим заново
        else:
            s2 = s
        text = text.replace(s,alphabet[int(s2)-1])
        #print(text)
        #при замене необходимо сдвинуться по строке в обратно
        #на количество заменяемых символов, что бы не пропустить символы после замены
        if len(s) > 1:
            i -= len(s) - 1
        s = ""
print(text)