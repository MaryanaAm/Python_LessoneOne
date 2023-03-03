# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5
import random

length = 25
lst = [random.randint(1, 25) for _ in range(length)]
print(lst)

min_dif = lst[0]
x = int(input('Введите искомое число:'))
for i in range(len(lst)):
    if abs(lst[i] - x < min_dif - x):
        min_dif = lst[i]

print(f'Ближайшее число: {min_dif}')


# length = 25

# lst = [random.randint(1, 25) for _ in range(length)]
# print(lst)

# x = int(input('Введите искомое число:'))
# lst.sort()
# count = 0
# for i in lst:
#     if i < x:
#         num = i
#     elif i > x:
#         break

# print(f'Наиболее близкое число: {num}')
