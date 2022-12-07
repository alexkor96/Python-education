# Задайте число N. Составьте список чисел Фибоначчи, N - количество чисел в списке
def fib(n) :
    if n in [1,2]:
        return 1
    else:
        return fib(n-1) + fib(n-2)
list = []
n = int(input('Введите количество чисел Фибоначи '))
for e in range(1,n+1):
    list.append(fib(e))
print(list)