# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.

# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 

def f_name(x, y):
    if y == 0:
        return 1
    return x * f_name(x, y-1)

print(f_name(3, 2))