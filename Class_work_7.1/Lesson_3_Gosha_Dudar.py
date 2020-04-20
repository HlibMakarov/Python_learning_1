                # Выбираем редактор кода: PyCharm
                # Книги:
                # 1)Byte of Python  150 стр Версия языка 3.0
                # 2)Грокаем алгоритмы 300 стр
                # 3)Проект Эйлера - вбить в голову навык построения алгоритмов. Решить первую сотню задач.
                # 4) Книга Изучаем пайтон Марка Луца и другую его книгу.


#https://youtu.be/Q7ccXmziG-I?list=PL0lO_mIqDDFXgfuxOEDTCwsWmKezOaDTu&t=189

#print(25%4)

#name = input("Как вас зовут")
#print("Привет,", name)

#test = 12
#print(test)

# https://youtu.be/j8AePyuLw38?list=PL0lO_mIqDDFXgfuxOEDTCwsWmKezOaDTu&t=171

# num_1 = float(input("Enter first num: "))
# num_2 = float(input("Enter second num: "))
# res = num_1 + num_2
# Res = input("Enter something: ")
# Res *= 5
# res += 5
# print("Result is", res, Res)

# https://youtu.be/tCSD-zNVkO4?list=PL0lO_mIqDDFXgfuxOEDTCwsWmKezOaDTu&t=47
# Урок №5 Условные операторы

# num = input("Введите ваше имя: ")
# if int(num) > 0:
#     if int (num) > 10:
#         print("вы ввели число больше 10")
#         if int (num) > 50:
#             print("вы ввели число больше 50")
#     else:
#         print("вы ввели число меньше 10 и больше 0")
# elif int (num) < -10:
#     print("вы ввели число меньше -10")
# else:
#     print("вы ввели число меньше 0 и больше -10")
# print ("All is okay!")
#
# name = input()
# A = 'Yes'   if name != "Test" else 'No'
# print(A)

# Урок №6 Циклы for,while а так же операторы
# https://youtu.be/6uSUQz3k_EM?list=PL0lO_mIqDDFXgfuxOEDTCwsWmKezOaDTu&t=40
# i = 1000
# while i > 100:
#     print(i)
#     i /= 2
#
# for j in 'hello world':
#     if j == 'a':
#         break
#     print(j * 2, end = '')
# else:
#     print("Буквы А нет в слове")

# Уроки Python для начинающих | #7 - Списки (list)
# https://youtu.be/ol23jnhVAOY?list=PL0lO_mIqDDFXgfuxOEDTCwsWmKezOaDTu&t=64

# l = []
# lis = [1, 56, 'x', 34, 2.34, ['S', 't', 'r', 'o', 'k', 'a']]
# print(lis)
# a = [a + b for a in 'list' if a != 's' for b in 'soup' if b != 'u']
# print(a)
#
# l.append(23)
# l.append(34)
# b = [24, 67]
# l.extend(b)
# l.insert(1, 56)
# l.append(34)
# l.remove(34)
# l.pop(0)
# print(l.index(56))
# print(l.count(34))
# l.sort()
# l.reverse()
# l.clear()
# print(l)

# Уроки Python для начинающих | #8 - Индексы и срезы
#  https://youtu.be/lFHwzZBweVg?list=PL0lO_mIqDDFXgfuxOEDTCwsWmKezOaDTu&t=18
# l = [34, 'sd', 56, 34.34]
#
# i = 0
# while i < 4:
#     print(l[i])
#     i += 1
#
# item[START:STOP:STEP]

# Уроки Python для начинающих | #9 - Кортежи (tuple)
# https://youtu.be/NgQzna6il2w?list=PL0lO_mIqDDFXgfuxOEDTCwsWmKezOaDTu&t=17

# a = (43, 56 ,45.23, 'd')
# b = [43, 56 ,45.23, 'd']
#
# print(a.__sizeof__())
# print(b.__sizeof__())

# a = ("hello world", "sdf", 345)
# print(a)
#
# print(a.count(345))

# Уроки Python для начинающих | #10 - Словари (dict), а также их методы
# https://youtu.be/NaA2H25gxN4?list=PL0lO_mIqDDFXgfuxOEDTCwsWmKezOaDTu&t=16
# d = dict ([(23, 34), (56, 87)])
#
# print(d)

# d = dict.fromkeys(['a', 'b', 'c'], 1)
#
# print(d)

# d = {a : a ** 2 for a in range (7)}
#
# print(d)
#
# d = {a : a ** 2 for a in range (7)}
# print(d)
#
# person = {'name' : {'last_name': 'Иванов', 'first_name': 'Иван',
# 'middle_name': 'Иванович'}, 'adress':
# ['г.Андрюшки', 'ул.Васильковская д.23б', 'кв.12'], 'phone':
# {'home_phone':'34-67-12', 'mobile_phone': '8-564-345-23-65',
#  'mobile_phone_2': 'нет'}}
# print(person['phone']['mobile_phone'])
# print(person.keys())

# Уроки Python для начинающих | #11 - Множества (set и frozenset)
# https://youtu.be/Q_AlNHNCXF4?list=PL0lO_mIqDDFXgfuxOEDTCwsWmKezOaDTu&t=61

# a = {i ** 2 for i in range (10)}
# a = {23}
# print(type(a))
# print(a)

# a = set ("Hello")
# b = frozenset ("Qwerty")
# a.add (1)
# print(a)

# a = ['r', 's', 'w', 'a', 's', 'w']
# print (a)
# print (set(a))

# a = {32, 45, 43.23, 76}
# x = {67, 45, 12, 43.23}
# a.clear()
# print(a)

# Уроки Python для начинающих | #12 - Функции (def, lambda, return)
# https://youtu.be/-vvQ_-JGzrM?list=PL0lO_mIqDDFXgfuxOEDTCwsWmKezOaDTu&t=14
#
# def func (**args):
#
#     return args
#
# print(func (short='dict', longer='dictionary'))
#
# add = lambda x, y: x * y
# print(add (2,5))

#  Уроки дальше
# https://youtu.be/T-DmoA08d3Y?list=PLvoBekrlHDgROfUUHMbrrdsy_b2y2V_rj&t=795
# name = input('Введите Ваше имя : ')
# count = input('Сколько раз  умножить : ')
#
# print(name * int(count))

# Python-джедай #4 - Типы данных, переменные
# https://youtu.be/5h-KmmxEMvA?list=PLvoBekrlHDgROfUUHMbrrdsy_b2y2V_rj&t=73

# test = 'Тестовая строка'
# test2 = 2.0
# print(test + str(test2))
#
# int число
# str строка
# float дробное

# print(float("210" * int("2")))
#
# test = 1
# test333 = 2
# test_test_test = 10
#
# test = 10
# Test = 20 регистрочувствителен разные переменные тест
# print(test)
# print(Test)
#
# test = 10
# del test
# print(test)

# #Метасинтаксические переменные
# foo -
# bar -

#Inplace data
#
# test = 10
# test +=10
# print(test)
#
# +=
# -=
# *=
# /=
# %=
#
# test = 10
# test /=2
# print(test)

# x = 4
# x *= 3
# print(x)
#
# x = 'Test'
# x *= 3
# print(x)
#
# test = 10
# test += 1
# print(test)

# Python-джедай #5 - Управляющие структуры
#  https://youtu.be/BVHhfQgRmuE?list=PLvoBekrlHDgROfUUHMbrrdsy_b2y2V_rj&t=12
# Булевые значения
# test = True
# test2 = False
# print(10 == 11) # equal
# print(10 != 11) # no equal
# print(15 > 10) # more or not
# print(5 >= 5) # more + equal

# Лексиграфическое сравнение
# Test #Чем дальше буква в алфавите тем больше у нее значение
# Tesa #, но также важна и позиция его в слове.
# print("Test" > "Tesa")
# # print(8.7 <= 8.7)
# pogoda = 'Winter'
# if pogoda == 'Winter':
#     print("At now is cold")

# pogoda = 'Winter'
# time = 'Day'
# print('Start program')
# if pogoda == 'Winter':
#     print("At now is cold")
#     if time == 'Night':
#         print("Crazy don`t walk at night!!!")
#     if time == 'Day':
#             print("it is ok DAy! ")
# if pogoda == 'Rain':
#     print("UUU it is rain")
# if pogoda == "sunny":
#     print("it is sunny go to walk")
# print("Finish program")

# Управляющие конструкции
# time = 'Morning'
#
# if time == 'Night':
#     print('At now Night are you crazy?')
# elif time == 'Morning':
#     print(' it is morning ?')
# else:
#     print('All very well bro you could walk in the street')

# parol = input('Enter your password')
#
# if parol == '123':
#     print("WELCOME")
# else:
#     print('Wrong pass')

# Python-джедай #6 - Множественные условия, приоритетность операторов
#  https://youtu.be/eFmvvJXxs7g?list=PLvoBekrlHDgROfUUHMbrrdsy_b2y2V_rj
#
# pogoda = 'Rain'
# time = 'Day'
# if pogoda == 'Rain' and time == 'Night':
#     print("what happens")

# pogoda = 'rain'
# if not pogoda == 'rain':
#     print('what what')
#
#  if not True   :
#      print("1")
#  elif not (1 + 1 == 3):
#      print("2")
#  else:
#      print("3")
#      # правильный ответ 2
#
# 1) ()
# 2) Возведение в степень **
# 3) * /
# 4) + -
#
# # приоритетность операторов таблица https://prnt.sc/aq8vk5

# print(1 + 3 * 5 / 3 ** 5)

# Python-джедай #7 - Циклы
# #  https://youtu.be/7D4azTSKAwg?list=PLvoBekrlHDgROfUUHMbrrdsy_b2y2V_rj
#
# test = True
#
# while test:
#     print("Hello")
#     test = False

# i = 1
#
# while i <= 5:
#     print(i)
#     i = i + 1
#
# i = 3
# while i >= 0:
#     print(i)
#     i = i - 1

# i = 1
# while 1 == 1:
#     print("Hello, " + str(i))
#     i += 1

# i = 1
# while 1 == 1:
#     print("Hello, " + str(i))
#     i += 1
#     if  i == 10001:
#         break
#
# number = 0
# while number <= 100:
#     number += 1
#     if (number % 2) != 0:
#         continue
#     print("Четное число " + str(number))

# Python-джедай #8 - Списки
# https://youtu.be/iRZsMSvAVm8?list=PLvoBekrlHDgROfUUHMbrrdsy_b2y2V_rj

# test = ['a', 'b', 'c',[ 'd', 'e', 'f']]
# print(test[3][2])
#
# test = [1, 2, 3]
# print(test + [4, 5, 6])
#
# test = 'hello'
# print(test[4])

# test = [' Alex Mercer', 'Tony Stark', 'Lenny Flawes']
# if ' Alex Mercer' in test:
#     print(' Alex Mercer is in list')
#
# test = [1, 3, 8, 9]
# if 4 in test:
#     print("4")
# if 3 in test:
#     print('3')
#
# test = [1, 3, 8, 9]
# if 4 not in test:
#     print("4 is not in list")
# if 3 not in test:
#     print('3')
#
# test = []
# test.append('hello')
# test.append(3)
# test.append([1, 2, 3])
# print(test)
#
# words = ["hello"]
# words.append('world')
# print(words[1])

# test = [5, 3, 2, 5, 6, 7]
# test.append('5')
# print(" all " + str(len(test))+ ' elements')

# test = [5, 3, 2, 5, 6, 7]
# test.append('5')
# test.remove('5')
# print(" all " + str(len(test))+ ' elements')

# test = [1, 2, 3,]
# test.insert(1, 4)
# print(test)

# test = [1, 2, 3, 3, 5, 5, 4, 4, 4]
# test.reverse()
# print(test)

    # Python-джедай #9 - Диапазоны, Обход списков

# https://youtu.be/z7oT_0WN2Bg?list=PLvoBekrlHDgROfUUHMbrrdsy_b2y2V_rj

# numbers = list(range(50,101,2))
# print(numbers)
#
# numbers = [1, 2, 3, 4, 5]
# i = 0
# length = len(numbers) - 1
# while i <= length:
#     print(str(numbers[i]) + '!')
#     i += 1
#
# numbers = [1, 2, 3, 4, 5]
# for element in  numbers:
#     print(str(element) + '!')

# for test in range(15):
#     print('Hello')


