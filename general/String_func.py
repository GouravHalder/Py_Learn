s = 'Hello, world.'
print(repr(s))
print (str(1/7))
x,y=1,2
print (repr((x, y, ('spam', 'eggs'))))
foo=10
print (f"{foo=} is number") # great for debugging as it prints the varialble name
print (f"{foo!s} is number")
print (f"{foo!r} is number")

bugs = 'roaches'
count = 13
area = 'living room'
print(f'Debugging {bugs=} {count=} {area=}')

print('We are the {} who say "{}!"'.format('knights', 'Ni'))
print('This {food} is {adjective}.'.format(food='spam', adjective='absolutely horrible'))
print ('Hello {name}, the time is {time}'.format(name='GH', time='02:07am'))
print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred',other='Georg'))
llist=['bom','tom']
print('The story of {0}, {1}, and {other}.'.format(llist[0],llist[1],other='Georg'))


table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('{0[Dcab]}'.format(table))
print('{0}'.format(table))