from enum import Enum
class Triangle(Enum):
    Equal = "Правильный треугольник"
    Isoscale = "Равнобедренный треугольник"
    Regular = "Обычный треугольник"
    Squared = "Прямоугольный треугольник"
    NotATriangle = "Не треугольник"

def triangle(a: int, b: int, c: int):
    if (a == b) or (a == c):
        return Triangle.Equal
    elif a == b:
        return Triangle.Isoscale
    elif (a <= b + c) or (b <= a + c):
        return Triangle.Regular
    else:
        return Triangle.NotATriangle