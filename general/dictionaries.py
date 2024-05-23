"""dictionary as a set of key: value pairs, 
with the requirement that the keys are unique (within one dictionary). 
A pair of braces creates an empty dictionary: {}."""

tel = ({'jack': 4098, 'sape': 4139},{'bombie': 1111, 'bulai': 2222},{'bombie1': 3333, 'bulai2': 4444})
for x in tel:
    for name, number in x.items():
        print (f"{name} and {number}")
Ltel=list(tel)
Ltel.append(1)
print(Ltel)
