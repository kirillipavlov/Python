#Дана строка “123467”, но в ней пропущена одна цифра.
#Использую функцию, выведите на экран строку со вставленной цифрой.
text = "123467"
text2=""
i = 0
print(text)
while i < len(text)-1:
    if int(text[i+1]) == int(text[i])+1:
        text2 += text[i]
    else:
        text2 += text[i] + str(int(text[i])+1)
    i += 1
text2 += text[-1]
print(text2)