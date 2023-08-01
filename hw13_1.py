# Возьмите 1-3 задачи из тех, что были на прошлых
# семинарах или в домашних заданиях. Напишите к ним
# классы исключения с выводом подробной информации.
# Поднимайте исключения внутри основного кода. Например
# нельзя создавать прямоугольник со сторонами
# отрицательной длины.

class Rectangle:

    def __init__(self, w: float, h: float = None):
        self.width = w
        if h is None:
            self.heigth = w
        else:
            self.heigth = h

    def calc_perimeter(self):
        while True:
            try:
                if self.heigth > 0 and self.width > 0:
                    a = (self.width + self.heigth) * 2
                    return a
            except ValueError:
                pass
            return f'Значения высоты и ширины должны быть > 0'

    def calc_area(self):
        while True:
            try:
                if self.heigth > 0 and self.width > 0:
                    b = self.heigth * self.width
                    return b
            except ValueError:
                pass
            return f'Значения высоты и ширины должны быть > 0'


rez = Rectangle(7, -3)
rez1 = Rectangle(5.5)
print(rez.calc_perimeter())
print(rez.calc_area())
print(rez1.calc_perimeter())
print(rez1.calc_area())