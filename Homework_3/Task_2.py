# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# *Пример:*

# - [2, 3, 4, 5, 6] =>[12,15,16]      ([2*6, 3*5, 4*4]);
# - [2, 3, 5, 6] => [12,15]   ( [2*6, 3*5]) 
# В скобках пример, как это работает!!!


List = [int(i) for i in input('Введите элементы списка через пробел: ').split()]
  
New_list = []
a = int(round((len(List)+ 1)/2))
for i in range(a):
    result = List[i] * List[len(List) - 1 - i]
    New_list.append(result)

print(List)
print(New_list)





# n = int(input('Num: '))
# multiplications = [math.factorial(i) for i in range(1, n+1)] # к каждому числу от 1 до n
# # применяем факториал
# multiplications_string = [mult(i) for i in range(1, n+1)]
# print(f"List of multiplications: {multiplications}")
# print(f"List: {multiplications_string}")