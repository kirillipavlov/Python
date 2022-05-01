print ("hello")
#__add__ -> +
#__sub__ -> -
#__mul__ -> *
#__truediv__ -> /
#__floordiv__ -> //
#__mod__ -> %
#__lt__ -> <
#__gt__ -> >
#__le__ -> <=
#__ge__ -> >=
class Y:
    def __init__(self, y):
        self.y = y
    def __add__(self, y_):
        return self.y + y_.y

class T:
    def __init__(self, y):
        self.y = y
    def __lt__(self, y_):
        if self.y < y_.y:
            return "1 < 2"
        else:
            return "1 > 2"
    def __eq__(self, y_):
        if self.y == y_.y:
            return "1 = 2"
        else:
            return "1 != 2"


o1 = Y(3)
o2 = Y(4)
o3 = Y("sdsd")
o4 = Y("vcbv")
print(o1 + o2)
print(o3 + o4)
print()
o1 = T(3)
o2 = T(4)
o3 = T(5)
o4 = T(4)
print(o1 < o2)
print(o1 == o3)
print(o2 == o4)
