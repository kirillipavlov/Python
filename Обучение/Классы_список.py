class Person():
    def __init__(self, name):
        self.name = name
    def display_info(self):
        print("Привет, меня зовут", self.name)

class Auto():
    def __init__(self, name):
        self.name = name
    def move(self, speed_):
        print(self.name, "движется со скоростью", self.speed_)
