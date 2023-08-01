# Возьмите 1-3 задачи из тех, что были на прошлых
# семинарах или в домашних заданиях. Напишите к ним
# классы исключения с выводом подробной информации.
# Поднимайте исключения внутри основного кода. Например
# нельзя создавать прямоугольник со сторонами
# отрицательной длины.
class MyException(Exception):
    pass


class MyValueError(MyException):
    def __init__(self, w: float, h: float = None):
        self.width = w
        if h is None:
            self.heigth = w
        else:
            self.heigth = h

    def __str__(self):
        text = ''
        if self.width <= 0:
            text = 'Ширина меньше 0'
        elif self.heigth <= 0:
            text = 'Высота < 0'
        return f'Нельзя создавать прямоугольник со сторонами отрицательной длины. Неверный формат данных. {text}. Вы ввели ({self.width},{self.heigth})'


class Rectangle:

    def __init__(self, w: float, h: float = None):
        if w > 0:
            self.width = w
            if h is None:
                self.heigth = w
            elif h > 0:
                self.heigth = h
        else:
            raise MyValueError(w, h)

    def calc_perimeter(self):

        a = (self.width + self.heigth) * 2
        return a

    def calc_area(self):

        b = self.heigth * self.width
        return b


rez = Rectangle(-7)
print(rez.calc_perimeter())
print(rez.calc_area())
