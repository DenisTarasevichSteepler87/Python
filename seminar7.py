# def my_lambda(num):
#     return num_1 * num_2


# f = lambda num_1, num_2: num_1 * num_2
# print(f(23,34))


# func = lambda x: x ** 2
# iter_object = [234,456,78,890,243,546,67]

# print(*map(func, iter_object))


# map_list = []
# for item in iter_object:
#     map_list.append(func(item))
    
# func_2 = lambda x: x % 2 == 0 
# print(*filter(func_2, iter_object))

# filter_list = []
# for item in iter_object:
#     if func_2(item):
#         filter_list.append(item)


# Задача №47.
# 1) У вас есть код, который вы не можете менять (так часто бывает, когда код в глубине программы используется множество раз и вы не хотите ничего сломать): 

# transformation = <???>
# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
# transormed_values = list(map(transformation, values))

# Единственный способ вашего взаимодействия с этим кодом - посредством задания функции transformation.
# Однако вы поняли, что для вашей текущей задачи вам не нужно никак преобразовывать список значений, а нужно получить его как есть.
# Напишите такое лямбда-выражение transformation, чтобы transformed_values получился копией values.

# 2) Есть код:

# transformation = <???>
# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
# transformed_values = list(map(transformation, values))
# if values == transformed_values:
#          print(‘ok’)
# else:
#          print(‘fail’)

# - В переменную transformation нужно прописать такую функцию, что бы в переменной transformed_values получилась копия списка values

# trasformation = lambda x: x
# values = [1, 23, 42, 'asdfg']
# transformed_values = list(map(trasformation, values))
# if values == transformed_values:
#     print('ok')
# else:
#     print('fail')



#     Задача №47.
# 1) Планеты вращаются вокруг звезд по эллиптическим орбитам. 
# Назовем самой далекой планетой ту, орбита которой имеет самую большую площадь.
# Напишите функцию find_farthest_orbit(list_of_orbits), 
# которая среди списка орбит планет найдет ту, 
# по которой вращается самая далекая планета. 
# Круговые орбиты не учитывайте: вы знаете, 
# что у вашей звезды таких планет нет, 
# зато искусственные спутники были были запущены на круговые орбиты.
# Результатом функции должен быть кортеж, 
# содержащий длины полуосей эллипса орбиты самой далекой планеты.
# Каждая орбита представляет из себя кортеж из пары чисел - полуосей ее эллипса. 
# Площадь эллипса вычисляется по формуле S = pi*a*b, где a и b - длины полуосей эллипса.
# При решении задачи используйте списочные выражения. 
# Подсказка: проще всего будет найти эллипс в два шага:
# сначала вычислить самую большую площадь эллипса, 
# а затем найти и сам эллипс, имеющий такую  площадь. 
# Гарантируется, что самая далекая планета ровно одна

# 2) - Дан список размеров(длина, ширина) эллипсов 
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# Напишите функцию find_farthest_orbit(list_of_orbits), 
# которая находит площадь самого большого эллипса и возвращает кортеж
# с его размерами. Площадь эллипса вычисляется по формуле
# S = pi*a*b, где a и b – длины и ширина осей эллипса
# -   Площадь кругов учитывать не нужно,
# т.е если у эллипса a == b, то это круг.
# При решении задачи используйте списочные выражения.
# Гарантируется, что самый большой эллипс всего один.

# Ввод:
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(*find_farthest_orbit(orbits))

# Вывод: 
# 2.5 10
# 1 решение
# def find_farthest_orbit(list_of_orbits):
#     max_s = 0
#     for a, b in list_of_orbits:
#         s = 3.14 * a * b
#         if a != b and s > max_s:
#             max_s = s
#             result = a, b
#     return result


# # 2 решение
# def find_farthest_orbit(list_of_orbits):
#     list_of_orbits = list(filter(lambda sizes: sizes[0] != sizes[1], list_of_orbits))
#     print(list_of_orbits)
#     list_max_areas = [3.14 * a * b for a, b in list_of_orbits]
#     print(list_max_areas)
#     max_area = max(list_max_areas)
#     i_max_area = list_max_areas.index(max_area)
#     return list_of_orbits[i_max_area]
#     # return [list_of_orbits[i] for i in range(len(list_of_orbits)) if list_max_areas[i] == max_area][0]

# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(*find_farthest_orbit(orbits))


# Задача №51.  Напишите функцию same_by(characteristic, objects),
# которая проверяет, все ли объекты имеют одинаковое значение 
# некоторой характеристики, и возвращают True, если это так. 
# Если значение характеристики для разных объектов отличается - то False.
# Для пустого набора объектов, функция должна возвращать True.
# Аргумент characteristic - это функция, которая принимает объект
# и вычисляет его характеристику.

# Ввод:							            Вывод:
# values = [0, 2, 10, 6]		                  same
# if same_by(lambda x: x % 2 == 0, values):
# 	print(‘same’)
# else:
# 	print(‘different’)


# print(all([True, True, True, True]))
# print(all([True, False, True, True]))
# print(all([False, False, False, False]))
# print()
# print(any([True, True, True, True]))
# print(any([True, False, True, True]))
# print(any([False, False, False, False]))
# print()
# print(all([1, 2, 3, 4]))
# print(all([1, 0, 3, 4]))
# print(all([0, 0, 0, 0]))
# print()
# print(any([1, 2, 3, 4]))
# print(any([1, 0, 3, 4]))
# print(any([0, 0, 0, 0]))
# print()
# print(all(['dfg', 'sdf', 'sdf', 'cvb']))
# print(all(['dfg', '', 'sdf', 'cvb']))
# print(all(['', '', '', '']))
# print()
# print(any(['dfg', 'sdf', 'sdf', 'cvb']))
# print(any(['dfg', '', 'sdf', 'cvb']))
# print(any(['', '', '', '']))
# print()
# print(all([[''], ('',), {''}, ['']]))
# print(all([[''], [], [''], ['']]))
# print(all([{}, {}, {}, []]))
# print()
# print(any([[''], ('',), {''}, ['']]))
# print(any([[''], [], [''], ['']]))
# print(any([{}, {}, {}, []]))
# print()

# 1 решение

# def same_by(characteristics, objects):
#     check_0 = characteristics(objects[0])
      
#     for num in objects[1:]:
#         if check_0 != characteristics(num):
#             return False
        
#     return True    
             
# values = [3, 1, 1, 7]

# if same_by(lambda x: x % 2 == 0, values):
#     print('same')
# else:
#     print('different')

# # 2 решение

# def same_by_2(characteristics, objects):
#     res_set = {characteristics(num) for num in objects}
#     if len(res_set) <= 1:
#         return True  
#     return False

# values = [1, 2, 5, 11]

# if same_by_4(lambda x: x % 2 == 0, values):
#     print('same')
# else:
#     print('different')


# # 3 решение

# def same_by_3(characteristics, objects):
#     result = list(filter(characteristics, objects))
#     if objects == result or not result:
#         return True
#     return False

# values = [1, 2, 5, 11]

# if same_by_4(lambda x: x % 2 == 0, values):
#     print('same')
# else:
#     print('different')

# # 4 решение  

# def same_by_4(characteristics, objects):
#     result = list(map(characteristics, objects))
#     if all(result) == any(result):
#         return True
#     return False
    
# values = [1, 2, 5, 11]

# if same_by_4(lambda x: x % 2 == 0, values):
#     print('same')
# else:
#     print('different')

