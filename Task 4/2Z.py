# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
n = int(input('Введите N: '))
spisok = []
i = 2 
while i <=n:
    if n%i==0:
        spisok.append(i)
        n//=i
    else:
        i+=1
print(spisok)