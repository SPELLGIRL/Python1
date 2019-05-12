# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех
# точек. Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

import math


class Point:
    x, y = 0, 0

    def __init__(self, x: int, y: int):
        self.x, self.y = x, y

    def __str__(self):
        return str([self.x, self.y])


class Side:
    a, b = None, None

    def __init__(self, a: Point, b: Point):
        self.a, self.b = a, b

    def __str__(self):
        return f'Side: {self.a} -> {self.b}'

    @property
    def length(self):
        if self.a is not None and self.b is not None:
            vector = Point(self.b.x - self.a.x, self.b.y - self.a.y)
            value = math.sqrt((vector.x ** 2 + vector.y ** 2))

            return round(value, 2)
        else:
            return 0


class Triangle:
    def __init__(self, a: Point, b: Point, c: Point):
        self.a, self.b, self.c = a, b, c

    @property
    def ab(self):
        return Side(self.a, self.b).length

    @property
    def bc(self):
        return Side(self.b, self.c).length

    @property
    def ca(self):
        return Side(self.c, self.a).length

    def perimeter(self, full=True):
        p = round(self.ab + self.bc + self.ca, 3)

        return p if full else p / 2

    def area(self):
        p = self.perimeter(False)
        s = math.sqrt(p * (p - self.ab) * (p - self.bc) * (p - self.ca))

        return round(s, 3)

    def height(self):
        p = self.perimeter(False)
        ha = round(2 * self.area() / self.bc, 3)
        hb = round(2 * self.area() / self.ca, 3)
        hc = round(2 * self.area() / self.ab, 3)

        return f'{ha}, {hb}, {hc}'


my_triangle = Triangle(
    Point(1, 1),
    Point(4, 4),
    Point(6, 2)
)

print('*' * 10, 'Triangle', '*' * 10)
print(f'Площадь треугольника равна: {my_triangle.area()}')
print(f'Высоты треуголиника hA, hB, hC равны: {my_triangle.height()}')
print(f'Периметр треугольника равен: {my_triangle.perimeter()}')


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

class Trapeze:
    def __init__(self, a: Point, b: Point, c: Point, d: Point):
        self.a, self.b, self.c, self.d = a, b, c, d

    def __str__(self):
        return f'Trapeze: {self.a},{self.b},{self.c},{self.d}'

    @property
    def ab(self):
        return Side(self.a, self.b).length

    @property
    def ac(self):
        return Side(self.a, self.c).length

    @property
    def bd(self):
        return Side(self.b, self.d).length

    @property
    def bc(self):
        return Side(self.b, self.c).length

    @property
    def cd(self):
        return Side(self.c, self.d).length

    @property
    def da(self):
        return Side(self.d, self.a).length

    def perimeter(self):
        return round(self.ab + self.bc + self.cd + self.da, 3)

    def area(self):
        return round(1 / 2 * (self.bc + self.da) * math.sqrt(self.ab ** 2 - (
                ((self.da - self.bc) ** 2 + self.ab ** 2 - self.cd ** 2) / (
                2 * (self.da - self.bc))) ** 2), 3)

    @property
    def is_trapeze_iso(self):
        return True if self.ac == self.bd else False


my_trapeze = Trapeze(
    Point(1, 3),
    Point(2, 8),
    Point(5, 8),
    Point(6, 3)
)

print('*'*10, 'Trapeze', '*'*10)
print(
    f'Длины сторон трапеции равны: {my_trapeze.ab}, {my_trapeze.bc}, {my_trapeze.cd}, {my_trapeze.da}')
print(f'Периметр трапеции равен: {my_trapeze.perimeter()}')
print(f'Площадь трапеции равна: {my_trapeze.area()}')
print(
    f'Трапеция{" не " if not my_trapeze.is_trapeze_iso else " "}является равнобочной.')
