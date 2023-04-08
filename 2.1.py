
"""
Объявите в программе два класса Point и Rectangle. Объекты первого класса должны создаваться командой:
pt = Point(x, y)
где x, y - координаты точки на плоскости (целые или вещественные числа). При этом в объектах класса Point должны формироваться следующие локальные свойства:
__x, __y - координаты точки на плоскости.
и один геттер:
get_coords() - возвращение кортежа текущих координат __x, __y
Объекты второго класса Rectangle (прямоугольник) должны создаваться командами:
r1 = Rectangle(Point(x1, y1), Point(x2, y2))
или
r2 = Rectangle(x1, y1, x2, y2)
Здесь первая координата (x1, y1) - верхний левый угол, а вторая координата (x2, y2) - правый нижний. При этом, в объектах класса Rectangle (вне зависимости от способа их создания) должны формироваться следующие локальные свойства:
__sp - объект класса Point с координатами x1, y1 (верхний левый угол);
__ep - объект класса Point с координатами x2, y2 (нижний правый угол).
Также к классе Rectangle должны быть реализованы следующие методы:
set_coords(self, sp, ep) - изменение текущих координат, где sp, ep - объекты класса Point;
get_coords(self) - возвращение кортежа из объектов класса Point с текущими координатами прямоугольника (ссылки на локальные свойства __sp и __ep);
draw(self) - отображение в консоли сообщения: "Прямоугольник с координатами: (x1, y1) (x2, y2)". Здесь x1, y1, x2, y2 - соответствующие числовые значения координат.
Создайте объект rect класса Rectangle с координатами (0, 0), (20, 34).
"""


class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def get_coords(self):
        return self.__x, self.__y


class Rectangle:

    def __init__(self, a, b, c=None, d=None):
        self.__sp = self.__ep = None
        if isinstance(a, Point) and isinstance(b, Point):
            self.__sp = a
            self.__ep = b
        elif all(map(lambda x: type(x) in (int, float), (a, b, c, d))):
            self.__sp = Point(a, b)
            self.__ep = Point(c, d)

    def set_coords(self, sp, ep):
        self.__sp = sp
        self.__ep = ep

    def get_coords(self):
        return (self.__sp, self.__ep)

    def draw(self):
        print(f"Прямоугольник с координатами: {self.__sp.get_coords()} {self.__ep.get_coords()}")


rect = Rectangle(0, 0, 20, 34)
rect.draw()


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_obj(self, obj):
        if self.tail:
            self.tail.set_next(obj)
        obj.set_prev(self.tail)
        self.tail = obj
        if not self.head:
            self.head = obj

    def remove_obj(self):
        if self.tail is None:
            return
        prev = self.tail.get_prev()
        if prev:
            prev.set_next(None)
        self.tail = prev
        if self.tail is None:
            self.head = None

    def get_data(self):
        data_list = []
        h = self.head
        while h:
            data_list.append(h.get_data())
            h = h.get_next()
        return data_list


class ObjList:
    def __init__(self, data):
        self.__data = data
        self.__next = None
        self.__prev = None

    def set_next(self, obj):
        self.__next = obj

    def set_prev(self, obj):
        self.__prev = obj

    def get_next(self):
        return self.__next

    def get_prev(self):
        return self.__prev

    def set_data(self, data):
        self.__data = data

    def get_data(self):
        return self.__data


lst = LinkedList()
lst.add_obj(ObjList("данные 1"))
lst.add_obj(ObjList("данные 2"))
lst.add_obj(ObjList("данные 3"))
res = lst.get_data()


from random import randint
from string import ascii_lowercase, digits, ascii_uppercase


class EmailValidator:
    EMAIL_CHAIRS = ascii_lowercase + digits + ascii_uppercase + '._@'
    EMAIL_CHAIRS_RANDOM = ascii_lowercase + digits + ascii_uppercase + '_'

    def __new__(cls, *args, **kwargs):
        return None

    @classmethod
    def get_random_email(cls):
        return ''.join(cls.EMAIL_CHAIRS_RANDOM[randint(0, (len(cls.EMAIL_CHAIRS_RANDOM) - 1))] for i in
                       range(randint(4, 20))) + '@gmail.com'

    @classmethod
    def check_email(cls, email):
        if not cls.__is_email_str(email):
            return False
        if not set(email) < set(cls.EMAIL_CHAIRS):
            return False
        s = email.split('@')
        if len(s) != 2:
            return False
        if len(s[0]) > 100 or len(s[1]) > 50:
            return False
        if '.' not in s[1]:
            return False
        if email.count('..') > 0:
            return False

    @staticmethod
    def __is_email_str(email):
        return type(email) == str


res = EmailValidator.check_email("sc_lib@list.ru") # True
print(res)
res = EmailValidator.check_email("sc_lib@list_ru") # False
print(res)
res = EmailValidator.check_email("sc..lib@list.ru")
print(res)
