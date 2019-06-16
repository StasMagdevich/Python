

'''
1.
(a + b * c)2;
a - 4 * b / c;
(a * b + 4) / (c - 1)

query1 = '(a + b * c)**2'
a = int(input('Введите число '))
b = int(input('Введите число '))
c = int(input('Введите число '))

result = (a + b * c)**2
print('The result for query: {}'.format(result))


query2 = 'a - 4 * b / c'
a = int(input('Введите число '))
b = int(input('Введите число '))
c = int(input('Введите число '))

result = a - 4 * b // c
print('The result for query: {}'.format(result))


query3 = '(a * b + 4) / (c - 1)'
a = int(input('Введите число '))
b = int(input('Введите число '))
c = int(input('Введите число '))

result = (a * b + 4) // (c - 1)
print('The result for query: {}'.format(result))

--------------------------------------------------------------

2.
Найти произведение нечетных цифр пятизначного целого числа, введенного пользователем с клавиатуры

variable = input("Введите число")
result = 1
for a in variable:
    a = int(a)
    if a % 2 != 0:
        result *= a
print('Произвидение нечетных чисел = {}'.format(result))

-----------------------------------------------------------------------

3.
Создать программу, выводящую на экран ближайшее к 10 из двух чисел, введенных пользователем.
Например, среди чисел 8,5 и 11,45 ближайшее к десяти 11,45.

a = int(input('Введите число'))
b = int(input('Введите число'))
c = 10
if abs(c-a) > abs(c-b):
    print("Ближе к 10ти число: {}".format(b))
elif abs(c-a) < abs(c-b):
    print("Ближе к 10ти число: {}".format(a))

-------------------------------------------------------------------------

4.
Определить является ли строка изограммой

def isogram():
    string = input('Введите слово: ')
    for i in string:
        if string.count(i) > 1:
            return print('является')
    else:
        print('net')


isogram()

---------------------------------------------------------------------------

5.
Найти сумму десяти первых чисел ряда Фибоначчи

n = 10
a = 1
b = 1

i = 0
while i < n - 2:
    fib_sum = a + b
    a = b
    b = fib_sum
    i = i + 1

print(b)

----------------------------------------------------------------------------

6.
В одномерном списке поменять местами минимальный и максимальный элементы. Остальные оставить на своих местах.

def getIndex(array):
     imax = max(array)
     index_max_el = array.index(imax)
     first_el = array[0]
     array[0] = index_max_el
     array[index_max_el] = first_el
     print(array)

getIndex([1,2,3,4,5,6,7])

-----------------------------------------------------------------------------

'''
