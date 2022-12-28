# предложить улучшения кода для уже решённых задач:

# С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension
# (выбрать 3 любые)


# Решенная задача № 2:

# С использованием map

my_list = list(map(int, input('Введите числа, через пробел: ').split()))
print(sum(my_list[1::2]))