# Задача 32: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

from random import randint

def fillarray(n):
    list_1 = [randint(1,20) for _ in range(n)]
    print(list_1)
    return list_1
def list_of_index(arr):
    min_digit = int(input("Введите минимальное число выборки: "))
    max_digit = int(input("Введите максимальное число выборки: "))
    for i in range(len(arr)):
        if min_digit <= arr[i] <= max_digit:
            print(i, end=' ')
    return arr

new_list = fillarray(15)
show_index = list_of_index(new_list)