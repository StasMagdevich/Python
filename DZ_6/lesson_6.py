
#Написать программу показывающая наибольшую цифру случайно сгенерированного 12 ти-значного
#натурального числа
#a) c использованием строк
#b) без использования строк

#a)
a = input("введите натуральное число")
a=int(a)
m = (int(a))%10
a = a//10
while a > 0:
    if a%10 > m:
        m = a%10
    a = a//10
print(m)

#b)
a = int(input())
m = a%10
a = a//10
while a > 0:
    if a%10 > m:
        m = a%10
    a = a//10
print(m)



#--------------------------------------------------------------------

#Написать программу для поиска разницы между максимальным и минимальным числом среди num_limit
#случайно сгенерированных чисел в указанном числовом диапазоне.

import random
#может сделал не верно, но по другому хз как сгенерировать числа
a = [random.randint(0, 9) for i in range(random.randint(0, 9))]
print(a)
x1 = (min(a))
print(x1)
x2 = (max(a))
print(x2)
print('RESULT : ',x2-x1)


#--------------------------------------------------------------------
#Написать программу для поиска разницы сумм всех четных и всех нечетных чисел среди num_limit случайно
#сгенерированных чисел в указанном числовом диапазоне. Т.е. от суммы четных чисел вычесть сумму
#нечетных чисел.

'''
подскажи как сделать
я так понимаю что сначала мы должны сгенерировать числа, т.е. к примеру как в предыдущем задании, затем
нужно найти сумму нечетных чисел типа
for i in range(0, 15):
    if i % 2 != 0:
        sum += i

print(sum)


затем четных и затем от одного отнять другое ????
'''