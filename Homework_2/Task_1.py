# Напишите программу, которая принимает на вход вещественное число
# и показывает сумму его цифр.

# *Пример:*

# - 6782 -> 23
# - 0,56 -> 11

number = input("Введите число: ")

number = int(str(number).replace('.', ''))

def func(number):
    if number < 0:
        number = number * (-1)
    else:
        number = number
    return number

number = abs(number)

sum = 0
while number > 0:
    digit = number % 10
    sum += digit
    number //= 10
    
print("Сумма цифр числа равна:", abs(sum))