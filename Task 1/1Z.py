# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
weekday = int(input('Введите цифру дня недели: '))
if weekday > 0 and weekday<=5:
    print("Не выходной")
elif weekday > 5 and weekday<=7:
    print("Выходной")
else: 
    print("Некорректный диапазон")
