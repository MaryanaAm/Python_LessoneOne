# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     3
#     -> 1

a = int(input('Введите длину массива: '))
lst = []
for i in range(a):
    n = int(input('Заполните массив: '))
    lst.append(n)
# List_1 = [2,5,8,3,7,4,9,1,0,2,8,3,8,4,9,6]
print(*lst)

x = int(input('Введите число для проверки: '))
count = 0

for i in range(0, len(lst)):
    if x == lst[i]:
        count += 1
   
print(f' Вывод: {count} ')
