print("hello")


def decorator(func):

    def wrapper():
        print("Функция обертка")
        print("Оборачиваемая функция", func)
        print("Выполнение оборачиваемой функции:")
        func()
        print("Выходим из обертки")

    return wrapper


@decorator  # hello = decorator(hello)
def hello():
    print("hello")


def end():
    print("end")


hello()
print()
end()
