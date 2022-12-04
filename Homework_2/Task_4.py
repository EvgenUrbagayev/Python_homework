# Реализуйте алгоритм перемешивания списка.

import random
list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def mix_list(list_original):
    list = list_original[:]
    list_length = len(list)
    for i in range(list_length):
        index_aleatory = random.randint(0, 8)
        temp = list[i]
        list[i] = list[index_aleatory]
        list[index_aleatory] = temp
    return list

new_list = mix_list(list)
print("Исходный список: ", list)
print("Перемешанный список: ", new_list)