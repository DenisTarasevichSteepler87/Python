# Задача №25. Решение в группах
# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.

# Input: a a a b c a a d c d d

# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

# Для решения данной задачи используйте функцию
# .split()


# # # 1 решение
# input_data = "a a a b c a a d c d d"
# input_list = input_data.split()
# output = ""
# count_dict = {}
# for letter in input_list:
#     output += letter
#     if letter in count_dict:
#         count_dict[letter] += 1
#         output += f"_{count_dict[letter]}"
#     else:
#         count_dict[letter] = 0
#     output += " "


# print("a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2")
# print(output)


# 2 решение
# input_data = "a a a b c a a d c d d".split()
# result = {}

# for letter in input_data:
#     if letter in result:
#         print(f"{letter}_{result[letter]}", end=" ")
#     else:
#         print(letter, end=" ")
#     result[letter] = result.get(letter, 0) + 1

# 3 решение если нет нижнего подчеркивания
# input_data = "a a a b c a a d c d d".split()
# result = {}

# for letter in input_data:
#     print(f"{letter}{result.get(letter, '')}", end=" ")

#     result[letter] = result.get(letter, 0) + 1


# Задача №27. Решение в группах
# Пользователь вводит текст(строка). Словом считается
# последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом
# пробелов. Определите, сколько различных слов
# содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells

# Output: 13
# 1 решение
# text_string = "She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells"

# text1 = text_string.lower().split()
# print(len(set(text1)))


# Задача №29. Решение в группах
# Ваня и Петя поспорили, кто быстрее решит
# следующую задачу: “Задана последовательность
# неотрицательных целых чисел. Требуется определить
# значение наибольшего элемента
# последовательности, которая завершается первым
# встретившимся нулем (число 0 не входит в
# последовательность)”. Однако 2 друга оказались не
# такими смышлеными. Никто из ребят не смог до
# конца сделать это задание. Они решили так: у кого
# будет меньше ошибок в коде, тот и выиграл спор. За
# помощью товарищи обратились к Вам, студентам.

# 2 Описание -На вход программе подаются натуральные числа, как только
# пользователь введет 0 (ноль) ввод прекращается. Вывести наибольший
# элемент получившейся последовательности.
# Есть два кода ошибок, нужно определить где ошибок меньше.
# Ваня:
# n = int(input())
# max_number = 0
# while n != 0:
#     n = int(input())
#     if n > max_number:
#         max_number = n
# print(max_number)

# Петя:
# n = int(input())
# max_number = -1
# while n > 0:
#     n = int(input())
#     if max_number < n:
#         max_number = n
# print(max_number)

# решение
# Ваня:
# n = int(input())
# max_number = n   #1 max_number = 1000
# while n != 0:
#     n = int(input())
#     if max_number < n: #2 if max_number > n:
#         max_number = n
# print(max_number)

# Петя:
# n = int(input())
# max_number = -1
# while n > 0:  #1 while n < 0:
#     if max_number < n:
#         max_number = n #2 n = max_number
#     n = int(input()) #3 перенесли ввод данных за if
# print(max_number) #4 print(n)









# name, surname,hgfd = 'Titrmur', 'Guevtrhetrh'
# print('Имя:', name, 'Фамилия:', surname)
name1 = 'Timur'
name2 = 'Gvido'
print(name1, name2)
name1, name2 = name2, name1
print(name1, name2)