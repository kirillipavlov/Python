class Person:
    name = "Tom"

    def display_info(self):
        print("Привет, меня зовут", self.name)


per1 = Person()
per1.display_info()
per2 = Person()
per2.name = "Bob"
per2.display_info()

print("**********")


class Person2:
    name = "Tom"

    def __init__(self, name_):
        self.name = name_

    def __del__(self):  #деструктор
        print(self.name, "удален из памяти")

    def display_info(self):
        print("Привет, меня зовут", self.name)


per1 = Person2("Bob")
per1.display_info()
per2 = Person2("Sam")
per2.display_info()

del per1
del per2