from enum import Enum
class Triangle(Enum):
    Equal = "Правильный треугольник"
    Isoscale = "Равнобедренный треугольник"
    Regular = "Обычный треугольник"
    Squared = "Прямоугольный треугольник"
    NotATriangle = "Не треугольник"

def triangle(a: int, b: int, c: int):
    if (a <= 0) or (b <= 0) or (c <= 0):
        return Triangle.NotATriangle
    elif (a == b) and (a == c):
        return Triangle.Equal
    elif (a == b) or (a == c) or (b == c):
        if (a < b + c) and (b < a + c) and (c < a + b):
            return Triangle.Isoscale
        else:
            return Triangle.NotATriangle
    elif (a < b + c) and (b < a + c) and (c < a + b):
        return Triangle.Regular
    else:
        return Triangle.NotATriangle