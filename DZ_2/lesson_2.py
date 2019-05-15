
'''
# Найти результат выражения для произвольных значений a,b,c: a + b * ( c / 2 )

query = 'a + b * ( c / 2 )'

a = 2
b = 2
c = 2

result = a + b * (c / 2)

print('The result for query {0} = {1}'.format(query,result))

The result for query a + b * ( c / 2 ) = 4.0

----------------------------------'''

'''
#Найти результат выражения для произвольных значений a,b: (𝑎^2 + 𝑏^2) % 2

query = '(𝑎^2 + 𝑏^2) % 2'

a = 2
b = 2
c = 2

result = (a**2 + b**2) % 2

print('The result for query {0} = {1}'.format(query,result))

The result for query (𝑎^2 + 𝑏^2) % 2 = 0
    
----------------------------------'''

'''
#Найти результат выражения для произвольных значений a,b,c: ( a + b ) / 12 * c % 4 + b

query = '( a + b ) / 12 * c % 4 + b'

a = 2
b = 2
c = 2

result = ( a + b ) / 12 * c % 4 + b

print('The result for query {0} = {1:.2f}'.format(query,result))

The result for query ( a + b ) / 12 * c % 4 + b = 2.67
    
----------------------------------'''

'''
#Найти результат выражения для произвольных значений a,b,c: (a - b * c ) / ( a + b ) % c

query = '(a - b * c ) / ( a + b ) % c'

a = 2
b = 2
c = 2

result = (a - b * c ) / ( a + b ) % c

print('The result for query {0} = {1}'.format(query,result))

The result for query (a - b * c ) / ( a + b ) % c = 1.5

----------------------------------'''

'''
#Найти результат выражения для произвольных значений a,b,c: | a - b | /( 𝑎 + 𝑏)3 - cos( c )

import math
query = '| a - b | /( 𝑎 + 𝑏)3 - cos( c )'

a = 2
b = 2
c = 2

result = math.fabs(a - b)/(a + b)**3 - math.cos(c)

print('The result for query {0} = {1:.2f}'.format(query,result))

The result for query | a - b | /( 𝑎 + 𝑏)3 - cos( c ) = 0.42

----------------------------------'''

'''
#Найти результат выражения для произвольных значений a,b,c: ( 𝑙𝑛( 1 + 𝑐 ) / −𝑏 )^4+ | a |

import math
query = '( 𝑙𝑛( 1 + 𝑐 ) / −𝑏 )**4+ | a |'

a = 2
b = 2
c = 2

result = ( math.log( 1 + c ) / -b )**4+ math.fabs(a)

print('The result for query {0} = {1:.2f}'.format(query,result))

The result for query ( 𝑙𝑛( 1 + 𝑐 ) / −𝑏 )**4+ | a | = 2.09
----------------------------------'''

