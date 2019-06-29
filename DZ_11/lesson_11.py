'''1. В текстовый файл построчно записаны фамилия и имя учащихся
класса и его оценки. Вывести на экран всех учащихся, чей
средний балл меньше 3 и посчитать средний балл по классу.



file = open("D:\Python_DZ\Python\DZ_11\class_magazine.txt")
counter = 0
summa = 0
for line in file:
    counter += 1
    length_line = len(line)
    for i in range(length_line):
        if line[i].isdigit():
            num = int(line[i])
            summa += num
            if num < 3:
                print("средний бал по классу меньше 3:", line)
            break

srednee_zna4 = counter//summa
print("\nСредний бал по классу:", srednee_zna4)


---------------------------------------------------------------'''
'''
2. Создать текстовый файл, записать в него построчно данные, 
которые вводит пользователь. Окончанием ввода пусть служит пустая 
строка.

file = input('Файл: ')
f = open(file,'w')
while True:
    k = input()
    if k == '': break
    f.write(k+'\n')
f.close()

-------------------------------------------------------------'''
'''
3. В текстовом файле посчитать количество строк, а также для каждой
отдельной строки определить количество в ней символов и слов.'''

file = open('D:\Python_DZ\Python\DZ_11\class_magazine.txt')
line = 0
for i in file:
    line += 1
    to4ka = 0
    word = 0
    for j in i:
        if j != ' ' and to4ka == 0:
            word += 1
            to4ka = 1
        elif j == ' ':
            to4ka = 0

    print(i, len(i), 'символов', word, 'слов')

print(line, 'строк')
file.close()

