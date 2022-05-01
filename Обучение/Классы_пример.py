class Employee:
    """Базовый класс для всех струдников"""
    emp_count = 0
    def __init__(self, name_, salary_):
        self.name = name_
        self.salary = salary_
    def display_count(self):
        print("Всего сотрудников:", self.emp_count)
    def display_employee(self):
        print("Имя", self.name, "Зарплата", self.salary)
    def __del__(self): #деструктор
        print(self.name, "удален из памяти")

"""print(Employee.__doc__)
print(Employee.__name__)
print(Employee.__module__)
print(Employee.__dict__)"""

from myclass import Person, Auto
tom = Person("Tom")
tom.display_info()
car = Auto("Audi")
car.move(100)
