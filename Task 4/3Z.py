# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
n1 = [1,2,3,1,2,3,45,6,5,3,4]
res = []
for i in n1:
    if n1.count(i)<2:
        res.append(i)
print(res)