'''
1. Из словаря:
	{'apple': ['malum', 'pomum', 'popula'], 'fruit': ['baca', 'bacca', 'popum'], 'punishment': ['malum', 'multa']}

создать словарь:
	{'baca': ['fruit'], 'bacca': ['fruit'], 'malum': ['apple', 'punishment'], 'multa': ['punishment'], 'pomum': ['apple'], 'popula': ['apple'], 'popum': ['fruit']}

from pprint import pprint as pp
d = {
    'apple': ['malum', 'pomum', 'popula', '2'],
    'fruit': ['baca', 'bacca', 'popum', '2'],
    'punishment': ['malum', 'multa']
}
r = {}
pp(d)
for key, values in d.items():
    for value in values:
        if value in r:
            r[value].append(key)
        else:
            r[value] = [key]

print()
pp(r)
------------------------------------------------------------

2. Создайте словарь, связав его с переменной school, и наполните данными, которые бы отражали количество учащихся в разных классах (1а, 1б, 2б, 6а, 7в и т. п.).
Внесите изменения в словарь согласно следующему: а) в одном из классов изменилось количество учащихся, б) в школе появился новый класс, с) в школе был расформирован (удален) другой класс.
Вычислите общее количество учащихся в школе. Новый словать не создавать, все изменения выполняются в исходном словаре.
s=0
school={'1a':21,'1b':29,'2a':30,'2b':27}
school['1a']=school['1a']-3
school['3a']=33
del school['1b']
for i in school:
    s=s+school[i]
print("В школе всего {} учеников".format(s))

---------------------------------------------------------------

3. Создайте словарь, где ключами являются числа, а значениями – строки.
Необходимо в данном словаре поменять местами ключ и значение, т. е. ключами являются строки, а значениями – числа.
Новый словать не создавать, все изменения выполняются в исходном словаре.'''


def change(vvod):
    v = {}
    for key, value in vvod:
        v[value] = key
    return v


x = {1: 'один', 2: 'два', 3: 'три'}
z = x.copy().items()
change(z)
print(x)
print(change(z))