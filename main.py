# Задача 30 a1, d, n,  an = a1 + (n-1)*d


a1 = int(input("Введите а1: "))
n = int(input("Введите n: "))
d = int(input("Введите d: "))
a = list()
for i in range(1, n):
    a.append(a1 + (i - 1) * d)
print(a)

# Задача 32:
import random

list1 = []
n_1 = int(input('Введите количество элементов: '))
for i in range(n_1):
        list1.append(random.randint(-20,20))
print(list1)

list_i = []
min_n = int(input('Введите начальное значение: '))
max_n = int(input('Введите конечное значение: '))
for i in range(len(list1)):
    if min_n <= list1[i] <= max_n:
        list_i.append(i)
print('Элементы под номерами: ', list_i, ' попадают в диапозон')
