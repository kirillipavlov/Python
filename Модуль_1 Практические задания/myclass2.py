class Student:
    def __init__(self, name):
        self.name = name
    def display_info(self):
        print("Привет, меня зовут", self.name)

class Subject:
    def __init__(self, sub):
        self.sub = sub
    def display_info(self):
        print("Я изучаю", self.sub)

class Emp(Student):
    def __init__(self, name, )