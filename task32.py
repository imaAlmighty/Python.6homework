# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

from random import randint
n = int(input('Enter length of array: '))
array = [randint(-100, 100) for i in range(n)]
print(array)
min_number = int(input('Enter the min number: '))
max_number = int(input('Enter the max number: '))
for i in range(len(array)):
    if min_number <= array[i] <= max_number:
        print(i)
