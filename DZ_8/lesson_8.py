
# Создайте список из всех нечётных чисел от 1 до 100 и передайте его в функцию,
#которая переставляет его элементы в случайном порядке (например, 99 11 43 19 … 7 91 3 1).
#Примечание: использовать метод random.shuffle не допускается.


numbers = range(1, 100)

def addOddNumbers(numbers):
    odd = []
    for num in numbers:
        if num % 2 == 1:
            odd.append(num)
            for i in range(len(odd) - 1, -1, -1):
                print(odd[i], end=' ')
#какаято херня получилась
# вроде выводит хаотично, но теперь у меня в списке не 100 значений, а наверное больше 10000 и они повторяются
#накосячил в цикле, но где, не могу допереть

addOddNumbers(numbers)



#------------------------------------------------------------------------------------------------------------------


#Сформировать возрастающий список из чётных чисел (количество элементов 45);

arr = list(range(0, 45, 2))
print (arr)


#------------------------------------------------------------------------------------------------------


# Найдите сумму и произведение элементов списка. Результаты вывести на экран
arr = [1,22,33,44,55,66,125]
print( 'SUMMA = ', sum((int(arr[i]) for i in range(int(len(arr))))))
def proizvidenie(arr):
    p = 1
    for n in arr:
        p *= n
    print('Произвидение =', p)


proizvidenie(arr)


#-------------------------------------------------------------------------------------------------------------------

# остальные хз как сделать
#особенно с шифрованием