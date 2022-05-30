# запись и дозапись в файл
# d = {
#     "Иванов Иван":[4,1,2,5,2],
#     "Петров Петр":[4,6,2,6,1],
#     "Сидоров Иван":[5,1,5,6,2]
#     }
# lst = [2, 4, 5, 1, 51, 2, 1]
# f = open("test1.txt", 'w', encoding='utf-8')
# for i in range(3):
#     s = input("enter string:")
#     f.write(s + "\n")
# f.write("hello world")
# f.write("help me \n")
# for el in lst:
#     f.write(str(el)+" ")
# for key,value in d.items():
#     f.write(key+":")
#     for el in value:
#         f.write(str(el)+" ")
#     f.write('\n')
# f.close()
# Считывание из файла данных
# try:
#     f = open('test1.txt','r',encoding='utf-8')
#     s = f.read()
#     # repr - позволяет увидеть сырую строку
#     # rstrip - убтрает \n \t \r в конце
#     s = s.replace('\n',' ').rstrip()
#     lst = s.split()
#     # s = s[:-1]
#     print(s)
#     print(lst)
#     f.close()
# except FileNotFoundError:
#     print('file not found')
# чтение данных из файла конструкция with as
# lst = []
# with open('test1.txt','r',encoding='utf-8') as f:
#     for line in f:
#         lst.extend(line.rstrip().split())
#     # s = f.readline().rstrip().split()
#     # lst.extend(s)
#     # s = f.readline().rstrip().split()
#     # lst.extend(s)
#     # s = f.readline().rstrip().split()
#     # lst.extend(s)
# print(lst)
# считать из файла и записать в словарь d
# d = {}
# with open('test1.txt','r',encoding='utf-8') as f:
#     for line in f:
#         key = line.rstrip().split(": ")[0]
#         value = line.rstrip().split(": ")[1].split(" ")
#         value = list(map(int,value))
#         d[key] = value
# print(d)
# Имеется текстовый файл.
# Переписать в другой файл все его строки
# с заменой в них символа 0 на символ 1 и наоборот.
# lst = []
# with open("test1.txt",'r',encoding='utf-8') as f:
#     for line in f:
#         lst.append(line.rstrip().split())
# for i in range(len(lst)):
#     for j in range(len(lst[i])):
#         print(lst[i][j],end=" ")
#     print()
# p = []
# for i in range(len(lst)):
#     for j in range(len(lst[i])):
#         p = list(lst[i][j])
#         for k in range(len(p)):
#             if p[k] =='0':
#                 p[k] = '1'
#             elif p[k] == '1':
#                 p[k] = '0'
#         lst[i][j] = "".join(p)
#         print(lst[i][j],end=" ")
#     print()
# print(lst)
# with open('test2.txt','w',encoding='utf-8') as f:
#     for el in lst:
#         s = ' '.join(el)
#         f.write(s+'\n')
# with open("C:\\Users\Denis\\test155.txt",'r',encoding='utf-8') as f:
#     s = f.read()
#     print(s)

# TASK 1
'''Создать текстовый файл и записать в него 6 строк.
Записываемые строки вводятся с клавиатуры. '''
# f = open("doc.txt", 'w', encoding='utf-8')
# for i in range(6):
#     st = input("Enter a string: ")
# #     f.write(st+'\n')
# f = open("doc.txt", 'r', encoding='utf-8')
# s = f.read()
# f.close()
# print(s)

# TASK 2
'''В конец существующего текстового файла записать три новые строки текста. 
Записываемые строки вводятся с клавиатуры.'''
# f = open("doc.txt", 'a', encoding='utf-8')
# for i in range(3):
#     st = input("Enter a string: ")
#     f.write(st+'\n')
# f.close()

# TASK 3
'''Дан текстовый файл. Подсчитать количество символов в нем без \n '''
# with open("doc.txt.",'r',encoding='utf-8') as f:
#     s = f.read().rstrip()
# print(len(s))

# TASK 4
'''Имеется текстовый файл, содержащий 5 строк. 
Переписать каждую из его строк в список в том же порядке'''
# with open("lines.txt",'r',encoding='utf-8') as file:
#     for line in file:
#         lst = []
#         lst.extend(line.rstrip().split())
#         print(lst)

# TASK 5
'''Имеется текстовый файл. 
Получить текст, в котором в конце каждой строки 
из заданного файла добавлен восклицательный знак'''
# with open("doc.txt",'r',encoding='utf-8') as file:
#     s = file.read().replace('\n', '!\n')
#     print(s)

# TASK 6
# with open("doc.txt",'r',encoding='utf-8') as file:
#     s = file.readlines()
#     length = 0
#     i = 0
#     for ind, el in enumerate(s):
#         if len(el) > length:
#             length = len(el)
#             i = ind
# print(f"Самая длинная строка: {s[i]}\nЕё длина: {length}\nЕё индекс: {i}")

# TASK 7

# with open("input.txt", 'w') as file:
#     numbers = input("Enter numbers: ")
#     file.write(numbers)
# with open("input.txt", 'r') as file, open("output.txt",'w') as f:
#     pr = 1
#     st = file.read().split()
#     st_int = [int(i) for i in st]
#     for num in st_int:
#         pr *= num
#     f.write(str(pr))

# TASK 8
# with open("doc.txt.",'r') as f, open("lines.txt", 'w') as f2, open("doc2.txt", 'w') as f3:
#     s = f.readlines()
#     for ind,el in enumerate(s):
#         if (ind+1) % 2 ==0:
#             f2.write(el)
#         else:
#             f3.write(el)

# TASK 9
# with open("doc.txt.",'r') as f, open("doc2.txt.",'r') as f2:
#     s = f.readlines()
#     s2 = f2.readlines()
#     mn = set(s)
#     length = len(mn)
# for ind,el in enumerate(s2):
#     mn.add(el)
#     if length != len(mn):
#         print('The strings arent the same. Number a string: ', ind+1)
#         break


# TASK 10
'''В справочной аэропорта хранится расписание вылета самолетов на следующие сутки. 
Для каждого рейса указаны номер рейса, пункт назначения, время вылета. 
Вывести все номера рейсов и время вылета самолета для заданного пункта назначения.'''

# НЕВЕРНОЕ РЕШЕНИЕ
#
# with open("23.05.2022.txt.",'r', encoding='utf-8') as file:
#     air = []
#     for row in file:
#         air.append(row.split())
#     print(air)
#     for i in range(len(air)):
#         for j in range(len(air)):
#             destination = input('Введите пункт назначения: ')
#             if destination == air[i][j]:
#                 print(air[i])
#             else:
#                 print('Нет рейсов на заданный пункт назначения')

# Second option   НЕПРАВИЛЬНОЕ

# with open("23.05.2022.txt.", 'r', encoding='utf-8') as file:
#     air = {}
#     for row in file:
#         key = row.rstrip().split("  ")[0]
#         value = row.rstrip().split("  ")[1].split(" ")
#         value = list(value)
#         air[key] = value
#     print(air)
#     for key,value in air.items():
#         destination = input('Введите пункт назначения: ')
#         if destination == value[0]:
#             print(key,value[1])


# РЕШЕНИЕ ДЕНИСА
# with open("plain.txt.",'r', encoding='utf-8') as file:
#     air = []
#     for row in file:
#         air.append(row.rstrip().split())
#     print(air)
#     find = False # проверка есть ли рейс вообще
#     destination = input('Введите пункт назначения: ')
#     for i in range(len(air)):
#         if destination in air[i]:
#             print(air[i])
#             find = True
#     if not find:
#         print('Нет рейсов на заданный пункт назначения')