# Линейные алгоритмы
# 
# 
# 1. Перевести граммы в килограммы и вывести 
# результат на экран. Значение граммов ввести с клавиатуры.

# a = input('Введите вес в граммах:')

# print (a + 'г это' + a/1000+'кг')


# a = int(input('Введите число:'))
# weight = (str(a/1000)+ 'кг')
# print(weight)

# 2. Даны две переменные x = 10 и y = 55. 
# Поменяйте их значения местами. 
# Выведите значения переменных на экран до и после замены.

# x = 10
# y = 55
# # print(f'{x, y}')

# x,y = y,x
# print(x, y)

# 3.С клавиатуры вводится расстояние L в метрах. 
# Необходимо найти и вывести на экран количество полных километров в нем. 


# L = int(input('Введите расстояние:'))
# KM = L / 1000 
# print(KM, 'километров')


# 4. С клавиатуры вводится целое число. 
# Необходимо вывести число, обратное введенному по порядку 
# составляющих его цифр. Например, если было введено число 12345, 
# программа должна вывести пользователю на экран число 54321.

# x =input('Введите число:')

# y = x[::-1]
# print('Обратное число', y)


# !!!!!!!!!! 5. Получите и преобразуйте текущую системную дату, 
# возвращаемую методом date.today() модуля стандартной 
# библиотеки datetime, из формата «год-месяц-день» в формат «день.месяц.год». 
# Выведите оба формата даты на экран.

# from datetime import date

# current_date = date.today()
# print(current_date)
# print('{}.{}.{}'.format(current_date.day, current_date.month, current_date.year))




# Логические выражения
# 1. Записать и вывести на экран условие, 
# которое является истинным, когда хотя бы одно из чисел x, y и z больше 80.

# x = int(input('Введите первое число:'))
# y = int(input('Введите второе число:'))
# z = int(input('Введите третье число:'))
# if x >=80:
#     print('Число', x, 'больше 80')
# if y >= 80:
#     print('Число', y, 'больше 80')
# if z >= 80:
#     print('Число', z, 'больше 80')
# else: 
#     print('Число меньше 80')

# 2. Записать и вывести на экран условие, которое является 
# истинным, когда оба числа a и b одновременно положительны или отрицательны.

# a = int(input('Введите число a:'))
# b = int(input('Введите число b:'))
# if a >=0 and b >=0:
#     print ('Числа', a, 'и', b, 'положительны')
# if a <=0 and b <=0:
#     print('Числа', a, 'и', b, 'отрицательны')
# else: 
#     print('Не одинаково положительны или отрицательны')

# 3. Даны три числа: 130, 25 и 70. Выведите на экран наименьшее из них, 
# использовав для этого программную проверку.
# a = 130
# b = 25
# c = 70

# if a<b<c:
#     print ('Наименьшее число', a)
# elif a>b>c:
#     print('Наименьшее число',c)
# else: 
#     print ('Наименьшее число',b)


# Циклы

# 1. Посчитайте количество символов в строке 'Python - это Питон!', 
# использовав счетчики на основе циклов for и while.

# text = 'Python - это Питон!'
# count = 0

# for i in range(len(text)): 
#     count += 1  
# print(count)



# 2. Найдите сумму всех элементов списка [1, '2', 3, 4, '5'], предварительно приводя строки к целым числам.

# strings = [1, '2', 3, 4, '5']

# numbers = list(map(int, strings))
# sum = 0
# for i in numbers:
#     sum += i
#     list= numbers[(numbers.index(i) - 1)]
# print (sum)

# 3. Используя циклы, проверьте при помощи оператора in наличие символов строки 'abcd\e123' 
# в строке 'bad_cat_23', выводя результаты проверки на экран в виде «Символ "a" есть в 
# "bad_cat_23".» или «Символа "n" нет в "bad_cat_23".».



# a = 'bad_cat_23'
# b = 'abcd\e123' 


# for j in b:
#     if j in a:
#         print(f'Символ {j} есть в "bad_cat_23".')
#     else:
#         print(f'Символа {j} нет в "bad_cat_23".')

#  task 3
# Cгенерируйте и выведите на экран мозаичное и
# зображение гексагональной сетки, напоминающее 
# мелкоячеистую проволочную сетку.

# for i in range(2, 15):
#     if i % 2 == 0:
#         for j in range (2, 15):
#             print('/ \_', end ='')
#         print('')

#     else: 
#         for i in range(2, 15):
#             print('\_/ ', end = '')
#         print('')


# 5. Выведите на экран таблицу умножения чисел от одного до девяти.

# numbers = [ i for i in range (1, 10)]
# print('----+----------------------------------------------------------------------------')
# print('| x |', end='\t')
# numbers_count = len(numbers) - 1
# for n in numbers:
#     if numbers.index(n) == numbers_count:
#         print(f'{n}', end= ' ')
#     else: 
#         print (f'{n}', end='\t')
# print('|')
# print('----+----------------------------------------------------------------------------')

# for i in numbers:
#    print(f'| {i} |', end = '\t')
#    for j in numbers:
#         print(f'{i * j:0>2d}', end= '\t')
        
#    print('')
# print('----+----------------------------------------------------------------------------')




# Функции 

# Напишите функцию, которая будет генерировать случайный пароль. 
# В пароле должно быть от 8 до 15 символов Юникода из диапазонов 48-57 (цифры), 
# 65-90 (буквы латинского алфавита в верхнем регистре) и 97-122 (буквы латинского алфавита в нижнем регистре). 
# Сгенерируйте и выведите на экран три пароля.
# import random
# num = input('login ')
# pas = ''
# for x in range(15): #Количество символов (16)
#     pas= pas + random.choice(list('48495051525354555657abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ')) 
#     pas2 = pas + random.choice(list('48495051525354555657abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ')) 
#     pas3 = pas + random.choice(list('48495051525354555657abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ')) 
   
# print('Hello, ', num, 'your first password is: ', pas)
# print('Hello, ', num, 'your second password is: ', pas2)
# print('Hello, ', num, 'your third password is: ', pas3)






# 1.
# 1 до 100 числа только кратные 5
# number_list = [i for i in range (1, 101) if i %5 == 0]

# print(number_list)

# 2.
# number_list = [i  for i in range (1, 21) if i >7 and i<9 ]

# print(number_list)