import math
s = int(input('Введите сумму чисел: '))
p = int(input('Введите произведение чисел: '))
x = (s - math.sqrt(s ** 2 - 4 * p)) / 2
y = s - x
print(math.ceil(x), math.ceil(y))
