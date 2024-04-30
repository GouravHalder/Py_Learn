"""dictionary as a set of key: value pairs, 
with the requirement that the keys are unique (within one dictionary). 
A pair of braces creates an empty dictionary: {}."""

tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
print (tel)
print (tel['jack'])
del (tel['sape'])
print (tel)
print (list(tel))
print (sorted(tel)) # sorts as per the Dict Keys
print ('guidoo' in tel)