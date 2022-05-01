"""
Создайте класс студентов
Создайте класс предметов
Используя новый проект, загрузите данные классов и задайте примеру двух студентов и двух направлений
"""
from myclass import Student, Subject
per = Student("Андрей")
per.display_info()
per = Subject("анатомию")
per.display_info()

per1 = Student("Виталий")
per2 = Subject("астрономию")

per1.display_info()
per2.display_info()