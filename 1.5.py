"""
1.5.  Инициализатор __init__ и финализатор __del__
"""

"""
Объявите класс Money так, чтобы объекты этого класса можно было создавать следующим образом:
my_money = Money(100)
your_money = Money(1000)
Здесь при создании объектов указывается количество денег, которое должно сохраняться в локальном свойстве (атрибуте) money каждого экземпляра класса.
P.S. На экран в программе ничего выводить не нужно.
"""


class Money:
    def __init__(self, money):
        self.money = money


my_money = Money(100)
your_money = Money(1000)

"""
Объявите класс Point так, чтобы объекты этого класса можно было создавать командами:
p1 = Point(10, 20)
p2 = Point(12, 5, 'red')
Здесь первые два значения - это координаты точки на плоскости (локальные свойства x, y), а третий необязательный аргумент - цвет точки (локальное свойство color). Если цвет не указывается, то он по умолчанию принимает значение black.
Создайте тысячу таких объектов с координатами (1, 1), (3, 3), (5, 5), ... то есть, с увеличением на два для каждой новой точки. Каждый объект следует поместить в список points (по порядку). Для второго объекта в списке points укажите цвет 'yellow'.

"""


class Point:
    def __init__(self, x, y, color='black'):
        self.x = x
        self.y = y
        self.color = color


points = []
for i in range(1, 2000, 2):
    if i == 3:
        p = Point(i, i, 'yellow')
        points.append(p)
    else:
        p = Point(i, i)
        points.append(p)

"""
Объявите три класса геометрических фигур: Line, Rect, Ellipse. Должна быть возможность создавать объекты каждого класса следующими командами:
g1 = Line(a, b, c, d)
g2 = Rect(a, b, c, d)
g3 = Ellipse(a, b, c, d)
Здесь в качестве аргументов a, b, c, d передаются координаты верхнего правого и нижнего левого углов (произвольные числа). В каждом объекте координаты должны сохраняться в локальных свойствах sp (верхний правый угол) и ep (нижний левый) в виде кортежей (a, b) и (c, d) соответственно.
Сформируйте 217 объектов этих классов: для каждого текущего объекта класс выбирается случайно (или Line, или Rect, или Ellipse). Координаты также генерируются случайным образом (числовые значения). Все объекты сохраните в списке elements.
В списке elements обнулите координаты объектов только для класса Line.
P.S. На экран в программе ничего выводить не нужно.
"""

import random


class Line:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)


class Rect(Line):
    ...


class Ellipse(Line):
    ...


a, b, c, d = [random.randint(0, 10) for _ in range(4)]
elements = [random.choice([Line(a, b, c, d), Rect(a, b, c, d), Ellipse(a, b, c, d)]) for _ in range(217)]
for i in elements:
    if isinstance(i, Line):
        i.sp = (0, 0)
        i.ep = (0, 0)

"""
Объявите класс TriangleChecker, объекты которого можно было бы создавать командой:
tr = TriangleChecker(a, b, c)
Здесь a, b, c - длины сторон треугольника.
В классе TriangleChecker необходимо объявить метод is_triangle(), который бы возвращал следующие коды:
1 - если хотя бы одна сторона не число (не float или int) или хотя бы одно число меньше или равно нулю;
2 - указанные числа a, b, c не могут являться длинами сторон треугольника;
3 - стороны a, b, c образуют треугольник.

Проверку параметров a, b, c проводить именно в таком порядке.
Прочитайте из входного потока строку, содержащую три числа, разделенных пробелами, командой:
a, b, c = map(int, input().split())
Затем, создайте объект tr класса TriangleChecker и передайте ему прочитанные значения a, b, c. Вызовите метод is_triangle() из объекта tr и выведите результат на экран (код, который она вернет).

Sample Input:
3 4 5
Sample Output:
3
"""


class TriangleChecker:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self):
        a, b, c = self.a, self.b, self.c
        if type(a) in (int, float) and type(b) in (int, float) and type(c) in (
        int, float) and a > 0 and b > 0 and c > 0:
            sort_list = sorted([self.a, self.b, self.c])
            if sort_list[0] + sort_list[1] > sort_list[2]:
                return 3
            else:
                return 2
        else:
            return 1


a, b, c = map(int, input().split())  # эту строчку не менять
tr = TriangleChecker(a, b, c)
print(tr.is_triangle())

"""
Объявите класс Graph, объекты которого можно было бы создавать с помощью команды:
gr_1 = Graph(data)
где data - список из числовых данных (данные для графика). При создании каждого экземпляра класса должны формироваться следующие локальные свойства:
data - ссылка на список из числовых данных (у каждого объекта должен быть свой список с данными, нужно создавать копию переданного списка);
is_show - булево значение (True/False) для показа (True) и сокрытия (False) данных графика (по умолчанию True);
В этом классе объявите следующие методы:
set_data(self, data) - для передачи нового списка данных в текущий график;
show_table(self) - для отображения данных в виде строки из списка чисел (числа следуют через пробел);
show_graph(self) - для отображения данных в виде графика (метод выводит в консоль сообщение: "Графическое отображение данных: <строка из чисел следующих через пробел>");
show_bar(self) - для отображения данных в виде столбчатой диаграммы (метод выводит в консоль сообщение: "Столбчатая диаграмма: <строка из чисел следующих через пробел>");
set_show(self, fl_show) - метод для изменения локального свойства is_show на переданное значение fl_show.
Если локальное свойство is_show равно False, то методы show_table(), show_graph() и show_bar() должны выводить сообщение:
"Отображение данных закрыто"
Прочитайте из входного потока числовые данные с помощью команды:
data_graph = list(map(int, input().split()))
Создайте объект gr класса Graph с набором прочитанных данных, вызовите метод show_bar(), затем метод set_show() со значением fl_show = False и вызовите метод show_table(). На экране должны отобразиться две соответствующие строки.
Sample Input:
8 11 10 -32 0 7 18
Sample Output:
Столбчатая диаграмма: 8 11 10 -32 0 7 18
Отображение данных закрыто
"""


class Graph():

    def __init__(self, data):
        self.data = data.copy()
        self.is_show = True

    def set_data(self, data):
        self.data = data

    def show_table(self):
        if self.is_show == False:
            print("Отображение данных закрыто")
        else:
            print(' '.join(str(i) for i in self.data))

    def show_graph(self):
        if self.is_show == False:
            print("Отображение данных закрыто")
        else:
            print(f"Графическое отображение данных: {' '.join(str(i) for i in self.data)}")

    def show_bar(self):
        if self.is_show == False:
            print("Отображение данных закрыто")
        else:
            print(f"Столбчатая диаграмма: {' '.join(str(i) for i in self.data)}")

    def set_show(self, fl_show):
        self.is_show = fl_show


data_graph = list(map(int, input().split()))
gr = Graph(data_graph)
gr.show_bar()
gr.set_show(fl_show=False)
gr.show_table()


"""
Объявите в программе следующие несколько классов:
CPU - класс для описания процессоров;
Memory - класс для описания памяти;
MotherBoard - класс для описания материнских плат.
Обеспечить возможность создания объектов каждого класса командами:
cpu = CPU(наименование, тактовая частота)
mem = Memory(наименование, размер памяти)
mb = MotherBoard(наименование, процессор, память1, память2, ..., памятьN)
Обратите внимание при создании объекта класса MotherBoard можно передавать несколько объектов класса Memory, максимум N - по числу слотов памяти на материнской плате (N = 4).
Объекты классов должны иметь следующие локальные свойства: 
для класса CPU: name - наименование; fr - тактовая частота;
для класса Memory: name - наименование; volume - объем памяти;
для класса MotherBoard: name - наименование; cpu - ссылка на объект класса CPU; total_mem_slots = 4 - общее число слотов памяти (атрибут прописывается с этим значением и не меняется); mem_slots - список из объектов класса Memory (максимум total_mem_slots = 4 штук по максимальному числу слотов памяти).
Класс MotherBoard должен иметь метод get_config(self) для возвращения текущей конфигурации компонентов на материнской плате в виде следующего списка из четырех строк:
['Материнская плата: <наименование>',
'Центральный процессор: <наименование>, <тактовая частота>',
'Слотов памяти: <общее число слотов памяти>',
'Память: <наименование_1> - <объем_1>; <наименование_2> - <объем_2>; ...; <наименование_N> - <объем_N>']
Создайте объект mb класса MotherBoard с одним CPU (объект класса CPU) и двумя слотами памяти (объекты класса Memory).
P.S. Отображать на экране ничего не нужно, только создать объект по указанным требованиям.
"""


class CPU:

    def __init__(self, name, fr):
        self.name = name
        self.fr = fr


class Memory:

    def __init__(self, name, volume):
        self.name = name
        self.volume = volume


class MotherBoard():
    def __init__(self, name, cpu, *mems):
        self.name = name
        self.cpu = cpu
        self.total_mem_slots = 4
        self.mem_slots = mems[:self.total_mem_slots]

    def get_config(self):
        ret = [f"Материнская плата: {self.name}",
               f"Центральный процессор: {self.cpu.name}, {self.cpu.fr}",
               f"Слотов памяти: {self.total_mem_slots}",
               f"Память: {'; '.join([f'{i.name} - {i.volume}' for i in self.mem_slots])}"]
        return ret


mb = MotherBoard('MBname', CPU('CPUname', 1111), Memory('Mname', 2222), Memory('M2name', 3333))

"""
Объявите в программе класс Cart (корзина), объекты которого создаются командой:
cart = Cart()
Каждый объект класса Cart должен иметь локальное свойство goods - список объектов для покупки (объекты классов Table, TV, Notebook и Cup). Изначально этот список должен быть пустым.
В классе Cart объявить методы:
add(self, gd) - добавление в корзину товара, представленного объектом gd;
remove(self, indx) - удаление из корзины товара по индексу indx;
get_list(self) - получение из корзины товаров в виде списка из строк:
['<наименовние_1>: <цена_1>',
'<наименовние_2>: <цена_2>',
...
'<наименовние_N>: <цена_N>']
Объявите в программе следующие классы для описания товаров:
Table - столы;
TV - телевизоры;
Notebook - ноутбуки;
Cup - кружки.
Объекты этих классов должны создаваться командой:
gd = ИмяКласса(name, price)
Каждый объект классов товаров должен содержать локальные свойства:
name - наименование;
price - цена.
Создайте в программе объект cart класса Cart. Добавьте в него два телевизора (TV), один стол (Table), два ноутбука (Notebook) и одну кружку (Cup). Названия и цены придумайте сами. 
P.S. Отображать на экране ничего не нужно, только создать объекты по указанным требованиям.
"""


class Cart:
    def __init__(self):
        self.goods = []

    def add(self, gd):
        self.goods.append(gd)

    def remove(self, index):
        self.goods.pop(index)

    def get_list(self):
        return [f"{i.name}: {i.price}" for i in self.goods]


class Table:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class TV:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Notebook:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Cup:
    def __init__(self, name, price):
        self.name = name
        self.price = price


cart = Cart()
cart.add(TV('tv1', 100))
cart.add(TV('tv2', 200))
cart.add(Table('table', 300))
cart.add(Notebook('nt1', 2000))
cart.add(Notebook('nt2', 2000))
cart.add(Cup('cup1', 30))


"""
Вам необходимо реализовать односвязный список (не список языка Python, объекты в списке не хранить, а формировать связанную структуру, показанную на рисунке) из объектов класса ListObject:
Для этого объявите в программе класс ListObject, объекты которого создаются командой:
obj = ListObject(data)
Каждый объект класса ListObject должен содержать локальные свойства:
next_obj - ссылка на следующий присоединенный объект (если следующего объекта нет, то next_obj = None);
data - данные объекта в виде строки.
В самом классе ListObject должен быть объявлен метод:
link(self, obj) - для присоединения объекта obj такого же класса к текущему объекту self (то есть, атрибут next_obj объекта self должен ссылаться на obj).
Прочитайте список строк из входного потока командой:
lst_in = list(map(str.strip, sys.stdin.readlines()))
Затем сформируйте односвязный список, в объектах которых (в атрибуте data) хранятся строки из списка lst_in (первая строка в первом объекте, вторая - во втором и  т.д.). На первый добавленный объект класса ListObject должна ссылаться переменная head_obj.
"""

import sys


# здесь объявляются все необходимые классы
class ListObject:
    def __init__(self, data):
        self.data = data
        self.next_obj = None

    def link(self, obj):
        self.next_obj = obj


# считывание списка из входного потока (эту строку не менять)
lst_in = list(map(str.strip, sys.stdin.readlines()))  # список lst_in в программе не менять

head_obj = ListObject(lst_in[0])
obj = head_obj

for i in range(1, len(lst_in)):
    new_obj = ListObject(lst_in[i])
    obj.link(new_obj)
    obj = new_obj
