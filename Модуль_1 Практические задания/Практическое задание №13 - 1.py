#Даны два параметра вывода “Я ученик”.
#Используя функцию def выведите на экран “Я лучший ученик Синергии!”
text = "Я ученик"
def modify():
    i1 = text.find("Я")
    i2 = text.find("ученик")
    print(text[:i1+1] + " лучший " + text[i2:] + " Синергии!")
modify()

#входные параметры для функции - (после какого слова, что вставляем)
def modify_(when, what):
    global text
    text = text[:text.find(when)+len(when)] + what + text[text.find(when)+len(when):]
modify_("Я"," лучший")
modify_("ученик"," Синергии!")
print(text)
