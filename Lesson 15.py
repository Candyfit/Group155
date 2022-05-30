# TASK 1
'''Список товаров, имеющихся на складе,
включает в себя наименование товара,
количество единиц товара, цену единицы и
дату поступления товара на склад.
Вывести список товаров, хранящихся больше месяца и
стоимость которых превышает 1 000 000 р'''

#
# with open("products.txt",'r', encoding='utf-8') as file:
#     lst = []
#     date = 0
#     for row in file:
#         lst.append(row.rstrip().split())
#     for el in lst:
#         v = el[4].split('.')
#         if ((int(v[1]) < 5 and int(v[0]) < 25) or (int(v[2]) < 2022)) or float(el[2]) >= 1000000:
#             print(*el)



# TASK 2
'''На АТС информация о разговорах содержит номер телефона абонента, 
время разговора и тариф. 
Вывести для заданного абонента сумму, 
которую ему следует оплатить за разговоры'''

#
# with open("ATS.txt",'r', encoding='utf-8') as file:
#     d = {}
#     for line in file:
#         key = line.rstrip().split(": ")[0]
#         value = line.rstrip().split(": ")[1].split(" ")
#         value = list(map(float,value))
#         d[key] = list(value)
#     person = input('Абонент: ')
#     for key, value in d.items():
#         if key == person:
#             print(d[key][1] * d[key][2], 'б.р.')



# TASK 3
'''Вам дается текстовый файл, 
содержащий некоторое количество непустых строк. 
На основе него сгенерируйте новый текстовый файл, 
содержащий те же строки в обратном порядке. 
Для решение вам необходимо открыть файл для чтения 3.txt .'''
# with open("3.txt",'r') as file:
#     s = file.readlines()
#     s = reversed(s)
#     print(*s)

# TASK 4
'''Написать программу “Викторина”. 
У вас есть 2 файла содержащих вопросы и 
ответы на данные вопросы. 
Пользователь отвечает на имеющиеся вопросы и 
затем программа показывает сколько правильных ответов было сделано'''

# with open("questions.txt.",'r', encoding='utf-8') as f, open("answers.txt.",'r', encoding='utf-8') as f2:
#     s = f.readlines()
#     s2 = f2.readlines()
#     count = 0
#     for ind, el in enumerate(s):
#         print(el)
#         answer = input('Введите ответ: ').capitalize()
#         if answer in s2[ind]:
#             print('Верно!')
#             count += 1
#         else:
#             print(s2[ind])
#     print(count)

# TASK 5
'''Дан кортеж. 
Найти наибольшее из чисел, которые встречаются ровно 2 раза'''
#
import random
# numbers = []
# tup = tuple([random.randint(1,6) for i in range(15)])
# print(tup)
# for num in tup:
#     if tup.count(num) == 2:
#         numbers.append(num)
# if len(numbers) > 0:
#     print(max(numbers))
# else:
#     print("Нет чисел по заданному условию.")

# TASK 6
'''Напишите программу, которая считывает текст из файла 
(в файле может быть больше одной строки) и 
выводит самое частое слово в этом тексте и 
через пробел то, сколько раз оно встретилось. 
Если таких слов несколько, вывести лексикографически первое. 
Для решение вам необходимо открыть файл для чтения 6.txt.
Слова, написанные в разных регистрах, считаются одинаковыми'''

# НЕПОЛНАЯ

# with open("6.txt",'r') as file:
#     s = file.read().lower().rstrip().split()
#     print(s)
#     d = {}
#     v = 0
#     for i in s:
#         x = s.count(i)
#         key = i
#         value = x
#         d[key] = value
#     for key, value in d.items():
#         if value > v:
#             v = value
#     for key, value in d.items():
#         if value == v:
#             print(key, d[key])

# TASK 7
'''Сгенерировать список из 30 чисел, 
заполнив его случайными значениями от 1 до 100. 
Вывести на экран числа которые являются полными квадратами. 
Числа кратные 5 записать в текстовый файл, остальные сложить. 
И вывести результат сложения на экран.'''

# lst =[random.randint(1,100) for i in range(10)]
# print(lst)
#
# with open("square_numbers.txt",'w') as file:
#     count = 0
#     for el in lst:
#         for j in range(1,11):
#             if el == j **2:
#                 print(el)
#         if el % 5 == 0:
#             file.write(str(el) + ' ')
#         if el != j **2 and el % 5 != 0:
#             count += el
# print(count)

