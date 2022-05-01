#text = "I loove Pyythhon!!!!!"
text = input("Введите строку: ")
s = ""
text += " "
#print(text)
for i in range(len(text)-1):
    if text[i] != text[i+1]:
        s += text[i]
print(s)