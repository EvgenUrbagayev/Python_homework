# Создайте программу для игры с конфетами человек против человека.
# *' Условие задачи: На столе лежит 117 конфета. Играют два игрока делая
# ход друг после друга. Первый ход определяется жеребьёвкой. За один ход
# можно забрать не более чем 28 конфет. Все конфеты оппонента достаются 
# сделавшему последний ход.

# a) Добавьте игру против бота

import random

player1 = input('Введите имя первого игрока: ')
player2 = input('Введите имя второго игрока: ')
igrok = random.randrange(1,3)
numbers = 117
if igrok == 1:
    print('Первый ход делает', player1)
else:
    print('Первый ход делает', player2)

while numbers > 0:
    if numbers > 28:
        player1 = int(input('Можно взять не более 28 конфет, сколько ты берешь?'))
        numbers = numbers - player1
        if numbers > 28:
            player2 = int(input('Можно взять не более 28 конфет, сколько ты берешь?'))
            numbers = numbers - player2
            if numbers <= 28:
                if igrok == 1:
                    print(f'Осталось {numbers} штук, их забирает и победил {player1}')
                else:
                    print(f'Осталось {numbers} штук, их забирает и победил {player2}')
            else:
                if igrok == 1:
                    print(f'Осталось {numbers} штук, их забирает и победил {player2}')
                else:
                    print(f'Осталось {numbers} штук, их забирает и победил {player1}')
