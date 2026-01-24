import math


def square(side):
    area = side * side
    if not isinstance(side, int):
        return math.ceil(area)
    else:
        return area


side = float(input("Укажите длинну стороны: "))

result = square(side)

print(f"Площадь квадрата = {result}")
