"""
Решите квадратное уравнение 5x**2-10*x-400=0 последовательно
сохраняя переменные a, b, c, d, x1 и x2.
"""

from math import sqrt

print('Решение квадратного уравнеия вида a*x**2+b*x+c=0')
a = float(input('введите значение a (с учетом знака): '))
b = float(input('введите значение b (с учетом знака): '))
c = float(input('введите значение c (с учетом знака): '))

d = b ** 2 - 4 * a * c

if d > 0:
    x1 = (-b + sqrt(d)) / (2 * a)
    x2 = (-b - sqrt(d)) / (2 * a)
    print(f'"Корни уравнения: x1 = {x1:.3f}; x2 = {x2:.3f}')
elif d == 0:
    x1 = -b / (2 * a)
    print(f'"Корень уравнения: x = {x1:.3f}')
else:
    print('Уравнение не имеет действительных корней')