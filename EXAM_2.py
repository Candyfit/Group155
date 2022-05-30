# TASK 1
''' Дан список. Выведите те его элементы, которые встречаются в списке только один
раз. Элементы нужно выводить в том порядке, в котором они встречаются в
списке'''
import random
# lst = [random.randint(1,16) for i in range(10)]
# print(lst)
# for el in lst:
#     if lst.count(el) == 1:
#         print(el)

# Task 2
''' Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
Считается, что любые два элемента, равные друг другу образуют одну пару,
которую необходимо посчитать'''


# lst = [random.randint(1,16) for i in range(10)]
# print(lst)
# count = 0
# for i in range(len(lst)):
#     for j in range(i + 1, len(lst)):
#         if lst[i] == lst[j]:
#             count += 1
# print(count)

# GFDGDFV

# a = [random.randint(1,10) for i in range(10)]
# print(a)
# print(sum(a.count(x) - 1 for x in a) // 2)

lst = [random.randint(1,16) for i in range(10)]
count = 0
print(lst)
for el in lst:
    if lst.count(el) % 2 == 0:
        count += lst.count(el)
        lst.remove(el)
print(count//2 if count > 2 else count)

# TASK 3
'''Даны два кортежа:
C_1 = (35, 78,21,37, 2,98, 6, 100, 231)
C_2 = (45, 21,124,76,5,23,91,234)
Необходимо определить:
1) Сумма элементов какого из кортежей больше и вывести соответствующее
сообщение на экран (Сумма больше в кортеже - ..)
2) Вывести на экран порядковые номера минимальных и максимальных элементов
этих кортежей'''

# C_1 = (35, 78,21,37, 2,98, 6, 100, 231)
# C_2 = (45, 21,124,76,5,23,91,234)
# s_1 = sum(C_1)
# s_2 = sum(C_2)
# if s_1 > s_2:
#     print('Сумма больше в кортеже - C_1')
# elif s_1 < s_2:
#     print('Сумма больше в кортеже - C_2')
# print(C_1.index(max(C_1)))
# print(C_1.index(min(C_1)))
# print(C_2.index(max(C_2)))
# print(C_2.index(min(C_2)))

# TASK 4
''' Создайте словарь из строки ' An apple a day keeps the doctor away' следующим
образом: в качестве ключей возьмите символы строки, а значениями пусть будут
числа, соответствующие количеству вхождений данной буквы в строку'''

# s = ' An apple a day keeps the doctor away'
# s = s.replace(' ','').lower()
# print(s)
# d = {}
# for el in s:
#     key = el
#     value = s.count(el)
#     d[key] = value
# print(d)

# TASK 5
'''Клиент приходит в кондитерскую. Он хочет приобрести один или несколько видов
продукции, а также узнать её состав.
Реализуйте кондитерскую.
У вас есть словарь, где ключ – название продукции (торт, пирожное, маффин и
т.д.). Значение – список, который содержит состав, цену (за 100гр) и кол-во (в
граммах).
Предложите выбор:
1. Если человек хочет посмотреть описание: название – описание
2. Если человек хочет посмотреть цену: название – цена.
3. Если человек хочет посмотреть количество: название – количество.
4. Всю информацию.
5. Приступить к покупке:
С клавиатуры вводите название торта и его кол-во. n – выход из программы.
Посчитать цену выбранных товаров и сколько товаров осталось в изначальном
списке
6. До свидания
'''

# sweet_shop = {"мармелад":["сахар, Е170, Е209, Е300, Е600", 2, 10000],"зефир":["сахар, яичный белок, Е100, Е200, Е309, Е609", 4, 10500],
#               "конфеты":["сахар, Е108, Е202, Е320, Е639", 10, 15000], "печенье":["мука, сахар, Е162, Е229, Е339, Е669", 3, 5000]}
# count = 0
# total_price = 0
# while True:
#     if count == 0:
#         choice1 = input('Добрый день! Какой товар интересует?\n').lower()
#         if choice1 == 'n':
#             break
#     else:
#         choice1 = input('Какой товар Вас еще интересует?\n').lower()
#         if choice1 == 'n':
#             break
#     if choice1 in sweet_shop:
#         choice2 = int(input('Хотите посмотреть состав? Введите - 1\n'
#                         'Хотите посмотреть цену? Введите - 2\n'
#                         'Хотите узнать количество товара, имеющееся в наличии? Введите - 3\n'
#                         'Хотите узнать всю информацию о продукте? Введите - 4\n'
#                         'Хотите приступить к покупке? Введите - 5\n'))
#         if choice2 == 1:
#             print(choice1,':', sweet_shop[choice1][0],)
#         if choice2 == 2:
#             print(choice1, '-', sweet_shop[choice1][1], 'б.р. за 100 гр.')
#         if choice2 == 3:
#             print(choice1, '-', sweet_shop[choice1][2], 'гр. в наличии')
#         if choice2 == 4:
#             print(choice1, ':', sweet_shop[choice1][0], 'цена', sweet_shop[choice1][1], 'за 100 гр.', sweet_shop[choice1][2], 'гр. в наличии')
#         if choice2 == 5:
#             amt = int(input('Сколько граммов хотите купить?\n'))
#             if amt > sweet_shop[choice1][2]:
#                 print('В наличии только', sweet_shop[choice1][2], 'граммов')
#                 choice3 = int(input('Хотите изменить вес? Введите - 1\n'
#                                     'Хотите выбрать другой товар? Введите - 2\n'))
#                 if choice3 == 1:
#                     amt = int(input('Сколько граммов хотите купить?\n'))
#                 if choice3 == 2:
#                     continue
#             price = amt / 100 * sweet_shop[choice1][1]
#             total_price += price
#             print('Стоимость: ', price, 'рублей')
#             weight = sweet_shop[choice1][2] - amt
#             sweet_shop[choice1][2] = weight
#     else:
#         print("Этого товара нет в наличии.")
#     count += 1
# print("Итоговая стоимость: ", total_price, 'рублей')
# print('До свидания! Приходите к нам еще :)')


# TASK 6
'''Даны два списка чисел. 
Посчитайте, сколько чисел содержится одновременно как в первом списке, так и во втором.'''
# lst = [random.randint(1,11) for i in range(5)]
# lst2 = [random.randint(1,11) for i in range(5)]
# print(len(set(lst).intersection(set(lst2))))

# TASK 7
'''Напишите программу, демонстрирующую работу try-except-finally'''

# file = open("doc.txt", 'r')
# d = {}
# for line in file:
#     key = line.rstrip().split(" ")[0]
#     value = line.rstrip().split(" ")[1]
#     d[key] = value
# try:
#     print(d['age'])
# except KeyError:
#     print('!KeyError!')
# finally:
#     file.close()


# TASK 8
'''В текстовый файл построчно записаны фамилия и имя учащихся класса и его
оценка за контрольную. Вывести на экран всех учащихся, чья оценка меньше 3
баллов и посчитать средний балл по классу'''

# with open("TASK_8.txt",'r', encoding='utf-8') as file:
#     d = {}
#     for line in file:
#         key = line.rstrip().split(": ")[0]
#         value = line.rstrip().split(": ")[1]
#         value = int(value)
#         d[key] = value
#     print(d)
#     mark = 0
#     for key in d:
#         mark += d[key]
#         if d[key] < 3:
#             print('Учащийся, чья оценка меньше 3 баллов:\n', key)
#             print()
#     print(mark // len(d), '- средний балл по классу.')
