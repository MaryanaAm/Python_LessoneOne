# Задача 2:

number = (input('Введите трехзначное число: '))
sum = int(number[0]) + int(number[1]) + int(number[2])
print(sum)

#или

num2 = int((input('Введите трехзначное число: ')))

print(num2 // 100 + num2 // 10 % 10 + num2 % 10 )