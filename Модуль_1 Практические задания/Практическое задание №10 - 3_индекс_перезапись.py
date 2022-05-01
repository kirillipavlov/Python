#Дана строка “123467”, но в ней пропущена одна цифра.
#Использую функцию, выведите на экран строку со вставленной цифрой.
text = "123467"
#text = "14689"
i = 0
print(text)
while i < len(text)-1:
    if int(text[i])+1 != int(text[i+1]):
        #print(i, text[i], text[:i+1], int(text[i])+1, text[i+1:])
        text = text[:i+1] + str(int(text[i])+1) + text[i+1:]
    i += 1
print(text)    
