# Создайте программу для игры с конфетами человек против бота
from random import *
import os


def player_vs_player():
    candies_total = 120
    max_take = 28
    count = 0 
    player_1 = input("Ваше имя: ")
    player_2 = input("Имя соперника: ")

    print("Первым будет ходить: ")

    x = randint(1,2)
    if x ==1:
        luc = player_1
        los = player_2
    else:
        luc = player_2
        los = player_1
    print(f'{luc} ходит первым. ')

    while candies_total>0:
        if count==0:
            step = int(input(f'Сколько вы возмете {luc} = '))
            if step > candies_total or step > max_take:
                step = int(input(f'Можно взять не больше{max_take} конфет {luc}, попробой еще раз: '))
            candies_total = candies_total-step
        if candies_total>0:
            print(f'на кону еще {candies_total}')
            count =1
        else:
            print('Конец игры')
        
        if count==1:
            step = int(input(f'Сколько вы возмете {los} = '))
            if step > candies_total or step > max_take:
                step = int(input(f'Можно взять не больше{max_take} конфет {los}, попробой еще раз: '))
            candies_total = candies_total-step
        if candies_total>0:
            print(f'на кону еще {candies_total}')
            count =0
        else:
            print('Конец игры')
    if count==1:
        print(f'{los} победил')
    if count==0:
        print(f'{luc} победил')
player_vs_player()
