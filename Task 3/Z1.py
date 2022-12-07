# Напишите программу, которая найдёт произведение пар чисел списка.  Парой считаем первый и последний элемент, второй и предпоследний и т.д.

lst1 = []
n = (int(input("kol-vo elementov: ")))
for i in range(0, n): 
    lst1.append((int(input())))
print(lst1)
newlst = []
for i in range((len(lst1)+1) //2):
   newlst.append(lst1[i]*lst1[-1-i])
print(newlst)