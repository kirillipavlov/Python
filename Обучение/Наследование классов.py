class Person:
    def __init__(self, name):
        self.__name = name
        self.__age = 1
    def set__age (self, age):
        if age > 0:
            self.__age = age
        else:
            print("Недопустимый возраст")
    def get__age(self):
        return self.__age
    def get__name (self):
        return self.__name
    def display_info(self):
        print("Имя:", self.__name, "Boзpacт:", self.__age)
############################################################
class Person2:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    @property
    def age (self):
        return self.__age
    #имя_свойства_блока_get.setter
    @age.setter
    def age (self, age):
        if age > 0:
            self.__age = age
        else:
            print("Недопустимый возраст")
    @property
    def name(self):
        return self.__name
    def display_info(self):
        print("Имя:", self.__name, "Boзpacт:", self.__age)
############################################################
class Employe (Person2):
    def details(self, company):
        print(self.name, "работает в компании", company)
"""
tom = Person("Tom")
tom.set__age(-17)
tom.set__age(23)
tom.display_info()
"""
"""
tom = Person2("Bob")
tom.age = -17
tom.age = 23
tom.display_info()
"""
tom = Employe("Bob", 24)
tom.details("ssd")
tom.age = 25
tom.display_info()