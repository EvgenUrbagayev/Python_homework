# предложить улучшения кода для уже решённых задач:

# С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension
# (выбрать 3 любые)


# Решенная задача № 1:

# number = int(input('Введите число: '))

# factorial = 1
# for i in range(number):
#     i = i + 1
#     factorial = i * factorial
    
#     print(factorial, end=" , ")

# С использованием лямбды

from math import factorial

n = int(input('Введите число: '))
print(list(map(lambda x: ((x == 1) and 1) or x * factorial(x -1),list(range(1,n+1)))))