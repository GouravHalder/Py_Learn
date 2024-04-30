knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)

for tup in knights.items():
    print(type(tup))

a,b="123a",2.45
print (type (a))
print (type (b))
l=['tic', 'tac', 'toe']
for i, v in enumerate(l):
    print(i, v)
for ii in enumerate(l):
    print(ii)
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
answers1 = ['lancelot', 'the holy grail', 'blue']

for q, a,w in zip(questions, answers,answers1):
    #print('What is your {0}?  It is {1}.'.format(q, a))
    print (q,a,w)
for i in range(1,10,2):
    print(i)
print("-----------------------")
for i in reversed(range(1, 10, 2)):
    print(i)

import math
raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filtered_data = [x for x in raw_data if not math.isnan(x)]
print (filtered_data)

string1, string2, string3 = '', '', 'Hammer Dance'
not_a_null = string1 or string2 or string3
print (not_a_null)
print (type("1, 2, 4, 8, 16".split(", ")))