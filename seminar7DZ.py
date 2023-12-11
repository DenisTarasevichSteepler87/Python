#Задача 34:Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм.
#Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает,
#Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв)
#в каждой фразе стихотворения одинаковое. Фраза может состоять из одного слова, если во фразе несколько слов,
#то они разделяются дефисами. Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух вбивает
#в программу с клавиатуры. В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”,
#если с ритмом все не в порядке
#Пример:
#Ввод: пара-ра-рам рам-пам-папам па-ра-па-дам
#Вывод: Парам пам-пам
# 1 решение
# def rhythm(str):
#     str = str.split()
#     list = []
#     for word in str:
#         result = 0
#         for i in word:
#             if i in 'аеёиоуыэюя':
#                 result += 1
#         list.append(result)
#     return len(list) == list.count(list[0])

# print('Введите: пара-ра-рам рам-пам-папам па-ра-па-дам')
# str = input()
# phrases = str.split()  # Разделяем фразы по пробелам
# if len(phrases) <= 1:  # Проверяем, что фраз больше одной
#     print("Количество фраз должно быть больше одной!")
# elif rhythm(str):
#     print('Парам пам-пам')
# else:
#     print('Пам парам')

#     2 решение GPT

# def check_rhythm(stroka):
#     phrases = stroka.split()  # Разделяем фразы по пробелам
#     if len(phrases) <= 1:  # Проверяем, что фраз больше одной
#         print("Количество фраз должно быть больше одной!")
#         return

#     syllable_counts = []  # Создаем список для хранения количества слогов во всех фразах
#     for phrase in phrases:
#         syllables = phrase.count('-') + 1  # Считаем слоги по количеству дефисов + 1
#         syllable_counts.append(syllables)  # Добавляем количество слогов в список

#     if len(set(syllable_counts)) == 1:  # Проверяем, одинаковое ли количество слогов во всех фразах
#         print("Парам пам-пам")
#     else:
#         print("Пам парам")

# print('Введите: пара-ра-рам рам-пам-папам па-ра-па-дам')
# str = input()




#Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
#которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца.
#Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны.
#Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля).
#Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, как, например,
#у операции умножения.
#Пример:
#Ввод:`print_operation_table(lambda x, y: x * y) `
#Вывод:
#1 2 3 4 5 6

#2 4 6 8 10 12
#3 6 9 12 15 18
#4 8 12 16 20 24
#5 10 15 20 25 30
#6 12 18 24 30 36

# def print_operation_table(operation, num_rows=2, num_columns=1):
#     if num_rows < 2 or num_columns < 2:
#         print("ОШИБКА! Размерности таблицы должны быть больше 2!")
#     else:
#         a = [[operation(i, j) for j in range(1, num_columns + 1)] for i in range(1, num_rows + 1)]
#         for i in a:
#             print(*[f"{x:>3}" for x in i])

# print_operation_table(lambda x, y: x * y)


def print_operation_table(operation, num_rows=9, num_columns=9): 
    result = [] 
    if num_rows < 2 or num_columns < 2: 
        print('ОШИБКА! Размерности таблицы должны быть больше 2!') 
    else: 
        print(' '.join([str(i) for i in range(1, num_columns + 1)])) 
        for i in range(2, num_rows + 1): 
            result.append(i) 
            for j in range(2, num_columns + 1): 
                if j != num_columns: 
                    result.append(f'{operation(i, j)} ') 
                else: 
                    result.append(operation(i, j)) 
            result.append('\n') 
        print(''.join([str(i) for i in result[:len(result) - 1]]))


# print_operation_table(lambda x, y: x * y)