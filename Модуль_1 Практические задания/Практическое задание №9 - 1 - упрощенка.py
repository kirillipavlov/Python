latin = "abcdefghijklmnopqrstuvwxyz"
#text = input("Введите строку: ")
text = "Hel12o 16e15ple"
#i = 0
s = ""
for a in text:
    if "0" <= a <= "9":
        s += a
        continue
    elif s != "":
        text = text.replace(s, latin[int(s)-1])
    s = ""
print (text)