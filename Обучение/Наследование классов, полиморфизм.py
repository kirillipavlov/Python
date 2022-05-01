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
    def __init__(self, name, age, company):
        Person2.__init__(self, name, age)
        self.company = company
    def display_info(self):
        Person2.display_info(self)
        print("работает в компании", self.company)
class Student (Person2):
    def __init__(self, name, age, univers):
        Person2.__init__(self, name, age)
        self.univers = univers
    def display_info(self):
        print("Студент", self.name, "учится в ", self.univers)

people = [Person2("Bob",18), Student("Sam", 25, "YDD"), Employe("Did", 27, "SSD")]
for per in people:
    per.display_info()
    print()