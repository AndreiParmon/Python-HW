# Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество
# элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: 
# a(n) = a(1) + (n-1) * d. Каждое число вводится с новой строки.
# Ввод:  7 2 5
# Вывод: 7 9 11 13 15

a = int(input('Введите первый эл-т: '))
d = int(input('Введите разность эл-тов: '))
n = int(input('Введите кол-во эл-тов: '))
num_n = []
for i in range(n):
    num_n = a + i * d
    print(num_n, end=' ')
