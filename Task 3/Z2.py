# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части
lst1 = []
n = (int(input("kol-vo elementov: ")))
for i in range(0, n): 
    lst1.append((float(input())))
print(lst1)
min = 1
max = 0
for i in lst1:
    if(i-int(i)) <= min:
        min = i - int(i)
    if(i-int(i)) >= max:
        max = i - int(i)
print(round(max-min,2))