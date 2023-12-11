# print(5, 8, 6)
# a= 1.68
# n= 5
# c= "cnhjrf"
# print('{}-{}-{}'.format(a,n,c))


# print("Введите 1 число")
# a=int(input())
# b=int(input("Введите 2 число"))
# print(a, "+",b, "=", a+b)


# c=1
# print(c)
# print(type(c))
# n=bool(c)
# print(type(n))
# print(n)

# a=1.5564646
# b=6.5464856
# print(round(a*b, 3))


# iter = 2
# iter += 3 # iter = iter + 3
# iter -= 4 # iter = iter - 4
# iter *= 5 # iter = iter * 5
# iter /= 5 # iter = iter / 5
# iter //= 5 # iter = iter // 5
# iter %= 5 # iter = iter % 5
# iter **= 5 # iter = iter ** 5

# a = 1 > 4
# print(a)

# a = 1 < 4 and 5 > 2
# print(a)

# a = 1 == 2
# print(a)

# a = 1 != 2
# print(a)

# a = 'qwe'
# b = 'qwe'
# print(a == b)

# a = 1 < 3 < 5 < 10
# print (a) 

# username = input('Введите имя: ')
# if username == 'Маша':
#     print('Ура, это же МАША!')
# elif username == 'Марина':
#     print('Я так ждала Вас, Марина!')
# elif username == 'Ильнар':
#     print('Ильнар - топ)')
# else:
#     print('Привет, ', username)


# n=654
# sum=0
# while n>0:
#     x=n%10
#     sum=sum+x
#     n=n//10
# else:    
#     print('Пожалуй')
#     print('хватит )')
# print(sum)    



# i = 0
# while i < 10:
#      if i == 3:
#         break
#      i = i + 1
# else:
#     print('Пожалуй')
#     print('хватит )')
# print(i)



# print("Введите число")
# n =int (input())
# flag = True
# i = 2
# while flag:
#     if n % i == 0: # если остаток при делении числа n на i равен 0
#         flag = False
#         print(i)
#     elif i > n // 2: # делить числа не может превышать введенное число, деленное на 2
#         print(n)
#         flag = False
#     i += 1

# for i in 1, 2, 3, 4, 7, 2, 1, 5, 0,0,0,1,2,0,0:
#     if i<=3:
#         print(i)
 




# for i in "qwerty":
#     print (i)
   

# a="qwerty"
# print(a[0],a[1],a[2],a[3],a[4],a[5])

# a=""
# for i in range(5):
#     a=""
    
#     for j in range(5):
#         a+="*"
#     print(a)   # печатает после цикла J     
   
#  a=""
# for i in range(5):
#     a=""
    
#     for j in range(5):
#         a+="*"
#         print(a)   # печатает весь цикла J   

# a=""
# for i in range(5):
#     a=""
    
#     for j in range(5):
#         a+="*"
# print(a)   # печатает только последний цикл    


# text = 'СъЕШЬ ещё этих МяГкИх французских булок'
# print(len(text)) # 39 считает символы
# print('ещё' in text) # True  находит текст
# print(text.lower()) # съешь ещё этих мягких французских булок перевод в нижний регистр
# print(text.upper()) # СЪЕШЬ ЕЩЁ ЭТИХ МЯГКИХ ФРАНЦУЗСКИХ БУЛОК  перевод в верхний регистр
# print(text.replace('ещё','ЕЩЁ')) # СъЕШЬ ЕЩЁ этих МяГкИх французских булок замена символов


# text = 'съешь ещё этих мягких французских булок'
# print(text[0]) # c
# print(text[1]) # ъ
# print(text[len(text)-1]) # к
# print(text[-1]) # к
# print(text[-5]) # б
# print(text[:]) # съешь ещё этих мягких французских булок
# print(text[:2]) # съ
# print(text[20:])
# print(text[len(text)-2:]) # ок
# print(text[2:9]) # ешь ещё
# print(text[6:-18]) # ещё этих мягких
# print(text[0:len(text):6]) # сеикакл            выискивается каждый шестой элемент
# print(text[::6]) # сеикакл                      выискивается каждый шестой элемент
# text = text[2:9] + text[-5] + text[:2] # ...
# print(text)


