# Красовская Наталья
# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.




# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()
 
list_fruits = ["яблоко", "банан", "киви", "арбуз"]

for num, fruit in enumerate (list_fruits):
	print (str(num) + '.  {:>10}'.format(fruit))

# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

first_list = {1,2,30,7,20}
second_list = {3,50,1,7}
final_list = first_list - second_list
print ('Первый список: ', first_list) 
print ('Второй список: ', second_list)
print ('Список без элементов из второго: ',final_list)

# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

numbers = [4,6,7,8,25,45,66,34]
print ('Исходный список', numbers)
new_numbers = []
for i in numbers:
    if i % 2 == 0:
        new_numbers.append(i / 4)
    else:
        new_numbers.append(i * 2)
print('Новый список', new_numbers)

# normal
#  Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]

import math

numbers = [2, -5, 8, 9, -25, 25, 4]
new_numbers = []
print('Исходный список', numbers)
for el in numbers:
   if el > 0 and (math.sqrt(el)) % 1 == 0:
        new_numbers.append(int(math.sqrt(el)))
print('Новый список', new_numbers)


# Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)

#data_input = int(input('Введите число: '))
#month_input = int(input('Введите месяц: '))
#year_input = int(input('Введите год: '))
#data = {'date': data_input, 'month': month_input, 'year': year_input}
#day_letters = {'01':'первое','02':'второе','03':'третье','04':'четвертое','05':'пятое','06':'шестое','07':'седьмое','08':'восьмое','09':'девятое','10':'десятое','11':'одинадцатое','12':'двенадцатое', '13':'тринадцатое','14':'четырнадцатое','15':'пятьнадцатое','16':'шестьнадцатое','17':'семнадцатое','18':'восемнадцатое','19':'девятнадцатое','20':'двадцатое','21':'двадцать первое','22':'двадцать второе','23':'двадцать третье','24':'двадцать четвертое','25':'двадцать пятое','26':'двадцать шестое','27':'двадцать седьмое','28':'двадцать восьмое','29':'двадцать девятое','30':'дридцатое','31':'тридцать первое'}
#month_letters = {'01':'января', '02':'февраля', '03':'марта', '04':'апреля', '05':'мая', '06':'июня','07':'июля', '08':'августа', '09':'сентября', '10':'октября', '11':'ноября', '12':'декабря'}
#year_letters = {'2018':'2018 год','2017':'2017 год','2019':'2019 год' }

#Не понимаю как словари объединить друг с другом

# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random

import random
elements = int (input('Введите количество элементов: '))
numbers = []
n = 0
while n < elements:
    numbers.append(random.randint(-100, 100))
    n +=1
print(numbers)


# Задача-4: Дан список, заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут: 
# а) неповторяющиеся элементы исходного списка:
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
# б) элементы исходного списка, которые не имеют повторений:
# например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]

lst = [1, 2, 4, 5, 6, 2, 5, 2]
print (lst)
lst2 = set(lst)
print('Неповторяющиеся элементы:', lst2)
