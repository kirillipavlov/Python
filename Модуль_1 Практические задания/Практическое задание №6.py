print("Введите значение веса в g, kg, t")
massa = input()
if massa[-2:] == "kg": 
    print (str(int(massa[:-2])*1000)+ "g")
    print (str(int(massa[:-2])/1000)+ "t")
elif massa[-1:] == "g":
    print (str(int(massa[:-1])/1000)+ "kg")
    print (str(int(massa[:-1])/1000000)+ "t")
elif massa[-1:] == "t":
    print (str(int(massa[:-1])*1000000)+ "g")
    print (str(int(massa[:-1])*1000)+ "kg")
else:
    print ("Не определена мера веса")