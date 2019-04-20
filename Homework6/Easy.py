# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех
# точек. Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

from math import sqrt


class Triangle:
    def __init__(self, a, b, c):
        self.__x1, self.__y1 = a
        self.__x2, self.__y2 = b
        self.__x3, self.__y3 = c
        self.__ab = sqrt(abs((self.__x2 - self.__x1) ** 2
                             + (self.__y2 - self.__y1) ** 2))
        self.__bc = sqrt(abs((self.__x3 - self.__x2) ** 2
                             + (self.__y3 - self.__y2) ** 2))
        self.__ac = sqrt(abs((self.__x3 - self.__x1) ** 2
                             + (self.__y3 - self.__y1) ** 2))

    @property
    def area(self):
        return round(abs(((self.__x2 - self.__x1) * (self.__y3 - self.__y1) -
                          (self.__x3 - self.__x1) * (self.__y2 - self.__y1)) / 2), 3)

    @property
    def height(self):
        ha = round(2 * self.area / self.__bc, 3)
        hb = round(2 * self.area / self.__ac, 3)
        hc = round(2 * self.area / self.__ab, 3)
        return ha, hb, hc

    @property
    def perimeter(self):
        return round(self.__ab + self.__bc + self.__ac, 3)


my_triangle = Triangle((1, 1), (4, 4), (6, 2))
print(f'Площадь треугольника равна: {my_triangle.area}')
print(f'Высоты треуголиника hA, hB, hC равны: {my_triangle.height}')
print(f'Периметр треугольника равен: {my_triangle.perimeter}')


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

class Trapeze:
    def __init__(self, a, b, c, d):
        self.__x1, self.__y1 = a
        self.__x2, self.__y2 = b
        self.__x3, self.__y3 = c
        self.__x4, self.__y4 = d

        def length(dot1: tuple, dot2: tuple) -> float:
            return round(
                sqrt(abs((dot2[0] - dot1[0]) ** 2 + (dot2[1] - dot1[1]) ** 2)), 3)

        self.ab = length(a, b)
        self.bc = length(b, c)
        self.cd = length(c, d)
        self.ad = length(a, d)
        self.ac = length(a, c)
        self.bd = length(b, d)

    @property
    def perimeter(self):
        return round(self.ab + self.bc + self.cd + self.ad, 3)

    @property
    def area(self):
        return round(1 / 2 * (self.bc + self.ad) * sqrt(self.ab ** 2 - (
                ((self.ad - self.bc) ** 2 + self.ab ** 2 - self.cd ** 2) / (
                2 * (self.ad - self.bc))) ** 2), 3)

    @property
    def is_trapeze_iso(self):
        return True if self.ac == self.bd else False


my_trapeze = Trapeze((1, 3), (2, 8), (5, 8), (6, 3))
print(
    f'Длины сторон трапеции равны: {my_trapeze.ab}, {my_trapeze.bc}, {my_trapeze.cd}, {my_trapeze.ad}')
print(f'Периметр трапеции равен: {my_trapeze.perimeter}')
print(f'Площадь трапеции равна: {my_trapeze.area}')
print(
    f'Трапеция{" не " if not my_trapeze.is_trapeze_iso else " "}является равнобочной.')
