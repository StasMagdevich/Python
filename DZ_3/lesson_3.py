# Преобразовать строку с американским форматом даты в европейский. Например, '05.17.2016' преобразуется в '17.05.2016'

t = '05.17.2016'

idx = t.find('.')

day = t[:idx]

idx1 = t.find('.', idx + 1)
month = t[idx+1: idx1]

year = t[idx1+1:]


result = month + '.' + day + '.' + year
print("date: " + result)

#date: 17.05.2016

#-----------------------------------------------------------------------------------------------------

#Дана строка с именем студента, в которой имя предшествует фамилии, например  'Mark Zuckerberg'.
# Написать программу, которая преобразует эту строку, ставя фамилию на первое место, а имя на второе.
# Т.е. 'Mark Zuckerberg' -> 'Zuckerberg Mark'

str1 = 'Mark Zuckerberg'

idx = str1.find(' ')

first = str1[:idx]

idx2 = str1.find(" ", idx + 1)
second = str1[idx+1: idx2]


result_ = second+" "+first
print(result_)

#Zuckerber Mark

#-----------------------------------------------------------------------------------------------



#Написать программу, которая преобразует имя переменной в формате snake_case в формат CamelCase.
# Для простоты считаем, что имя переменной всегда состоит из 3-х слов.
# Например: 'employee_first_name' -> 'EmployeeFirstName'

str2 = 'employee_first_name'

indx = str2.find('_')

word1 = str2[:indx]

idx1 = str2.find('_', indx + 1)
word2 = str2[indx+1: idx1]

word3 = str2[idx1+1:]

first = word1.capitalize()


second = word2.capitalize()


third = word3.capitalize()


print("result: " + first+second+third)

#result: EmployeeFirstName

#-----------------------------------------------------------------------------------------------

# Дана строка вида 'Leo Tolstoy*1828-08-28*1910-11-20'.
# В этой строке указаны имя писателя и через символ * даты рождения и смерти.
# Даты указаны в формате "YYYY-MM-DD".
# Требуется написать программу, которая по переданной строке определит возраст писателя и распечает его имя и возраст.
# Например, для строки 'Leo Tolstoy*1828-08-28*1910-11-20' программа должна распечает: 'Leo Tolstoy, 82'.
# Для строки: 'Marcus Aurelius*121-04-26*180-03-17' - 'Marcus Aurelius, 59'


string1 = 'Leo Tolstoy*1828-08-28*1910-11-20'
x = string1.find('*')
name = string1[:x]

y = string1.find('*', x + 1)
birth_year = string1[x+1: y]

z = string1.find('*', y + 1)
death = string1[y+1:]


indx1=birth_year.find('-')
date1=int(birth_year[:indx1])

indx2=death.find('-')
date2= int(death[:indx2])

age = str(date2-date1)

final_result = name + ', ' + age
print(final_result)

#Leo Tolstoy, 82

string2 = 'Marcus Aurelius*121-04-26*180-03-17'
x = string2.find('*')
name = string2[:x]

y = string2.find('*', x + 1)
birth_year = string2[x+1: y]

z = string2.find('*', y + 1)
death = string2[y+1:]


indx1=birth_year.find('-')
date1=int(birth_year[:indx1])

indx2=death.find('-')
date2= int(death[:indx2])

age = str(date2-date1)

final_result = name + ', ' + age
print(final_result)

#Marcus Aurelius, 59