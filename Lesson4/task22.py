# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений
# в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.
# Input:  11 6
#         2 4 6 8 10 12 10 8 6 4 2
#         3 6 9 12 15 18
# Output: 6 12


n = int(input('Введите кол-во N: '))
num_N = []
for i in range(n):
    num_N.append(int(input('Введите числа N: ')))
numbers1 = set(num_N)
print(num_N)

m = int(input('Введите кол-во M: '))
num_M = []
for i in range(m):
    num_M.append(int(input('Введите числа M: ')))
numbers2 = set(num_M)
print(num_M)

result = list(numbers1.intersection(numbers2))
result.sort()
print(result)
