# Задача №9. Решение в группах
# По данному целому неотрицательному n вычислите
# значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
# чисел от 1 до N) 0! = 1 Решить задачу используя цикл
# while
# Input: 5
# Output: 120


# n = input("Введите n : ")

# while not n.isdigit() or n == "0":
#     print("ошибка вввода: ")
#     n = input("Введите n : ")

# первое решение

# n = int(n)
# fact = 1
# num = 1
# while num <= n:
#     fact, num= fact*num, num+1
# print(fact)

# второе решение

# n = int(n)
# result = 1

# while n > 1:
#     result = result * n
#     n -= 1

# print(result)


# третье решение

# n = int(n)
# result = 1

# while n > 1:
#    result, n = result * n, n-1

# print(result)


#  Задача №11. Решение в группах
# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6

# a = input("Введите n : ")

# while not a.isdigit() or a == "0" or a == "1":
#     print("ошибка вввода: ")
#     a = input("Введите n : ")

# a = int(a)

# первое решение


# pos = 3
# pred = 1
# pred2 = 1
# while pred < a:
#     pred, pred2 = pred + pred2, pred
#     pos+=1
# if pred != a:
#     print(-1)
# else:
#     print(pos)

# второе решение

# pos = 3
# pred = 1
# pred2 = 1
# while pred < a:
#     temp = pred
#     pred = pred + pred2
#     pred2 = temp
#     pos += 1
# if pred != a:
#     print(-1)
# else:
#     print(pos)


# Задача №13. Решение в группах
# 1. Уставшие от необычно теплой зимы, жители решили узнать,
# действительно ли это самая длинная оттепель за всю историю
# наблюдений за погодой. Они обратились к синоптикам, а те, в
# свою очередь, занялись исследованиями статистики за
# прошлые годы. Их интересует, сколько дней длилась самая
# длинная оттепель. Оттепелью они называют период, в
# который среднесуточная температура ежедневно превышала
# 0 градусов Цельсия. Напишите программу, помогающую
# синоптикам в работе.
# Пользователь вводит число N – общее количество
# рассматриваемых дней (1 ≤ N ≤ 100). В следующих строках
# располагается N целых чисел.
# Каждое число – среднесуточная температура в
# соответствующий день. Температуры – целые числа и лежат в
# диапазоне от –50 до 50

# 2. Пользователь вводит число N(1 <= N <= 10). Далее построчно N от -50 до 50.
# Нужно вывести наибольшее количество идущих подряд положительных чисел

# Input: 6 -> -20 30 -40 50 10 -10
# Output: 2
# 1 решение когда положительных больше чисел
# import random

# days_num = int(input("Введите кол-во дней: "))

# max_thaw_days = 0
# thaw_days = 0
# for i in range(days_num):
#     # temperature = random.randint(-50, 50)  # включительно 50 и -50
#     temperature = int(input("Введите температуру: "))
#     # print(temperature, end=" ")
#     if temperature > 0:
#         thaw_days += 1
#     else:
#         if thaw_days > max_thaw_days:
#             max_thaw_days = thaw_days
#         thaw_days = 0

# if thaw_days > max_thaw_days:
#     max_thaw_days = thaw_days

# print()
# print(f"{max_thaw_days=}")
# """print(f"{2*3*5**2=}")


# 2 решение когда отрицательный больше чисел
# import random

# days_num = int(input("Введите кол-во дней: "))

# max_thaw_days = 0
# thaw_days = 0
# for i in range(days_num):
#     # temperature = random.randint(-20, 50)  # включительно 50 и -50
#     temperature = int(input("Введите температуру: "))
#     # print(temperature, end=" ")
#     if temperature > 0:
#         thaw_days += 1
#         if thaw_days > max_thaw_days:
#             max_thaw_days = thaw_days
#     else:
#         thaw_days = 0

# print()
# print(f"{max_thaw_days=}")


# Задача №15. Решение в группах
# 15. 1. Иван Васильевич пришел на рынок и решил
# купить два арбуза: один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз
# потяжелей, а для тещи полегче. Но вот незадача:
# арбузов слишком много и он не знает как же выбрать
# самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество
# арбузов. Вторая строка содержит N чисел,
# записанных на новой строчке каждое. Здесь каждое
# число – это масса соответствующего арбуза

# 2. Пользователь вводит одно число N. Далее идут N чисел,
# записанных на новой строчке каждое. Вывести максимальное и 
# минимальное (циклы)

# Input: 5 -> 5 1 6 5 9
# Output: 1 9

# 1 решение
# num = int(input("Введите число: "))
# min_weight = 1000
# max_weight = 0

# for _ in range(num):
#     weight = int(input("Введите весс: "))

#     if weight > max_weight:
#         max_weight = weight

#     if weight < min_weight:
#         min_weight = weight


# print(min_weight, max_weight)

# 2 решение
# from random import randint
# num = randint(1, 20)
# weight = randint(5, 15)
# print(weight, end=" ")
# min_weight = weight
# max_weight = weight

# for _ in range(num-1):
#     weight = randint(5, 15)
#     print(weight, end=" ")

#     if weight > max_weight:
#         max_weight = weight

#     if weight < min_weight:
#         min_weight = weight

# print()
# print(min_weight, max_weight)

# 3 решение
from random import randint

num = randint(1, 20)
weight = randint(5, 15)
print(weight, end=" ")
min_weight = weight
max_weight = weight

for _ in range(num-1):
    weight = randint(5, 15)
    print(weight, end=" ")
    max_weight = max(max_weight, weight) 
    min_weight = min(min_weight, weight) 


print()
print(min_weight, max_weight)