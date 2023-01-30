from math import sqrt

message = ('Добро пожаловать в самую лучшую программу для вычисления'
           'квадратного корня из заданного числа.')


def Calculate_Square_Root(Num):
    """Вычисляет квадратный корень."""
    return sqrt(Num)


def calc(your_number):
    """Принимает значение Num."""
    if your_number <= 0:
        result=Calculate_Square_Root(your_number)
        print(f'Мы вычислили квадратный корень из введённого вами числа.'
              f'Это будет: {result}')


print(message)
calc (25.5)