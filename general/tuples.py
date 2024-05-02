"""Tuples are immutable, and usually contain a heterogeneous sequence of elements 
that are accessed via unpacking (see later in this section) 
or indexing (or even by attribute in the case of namedtuples). 
Lists are mutable, and their elements are usually homogeneous 
and are accessed by iterating over the list."""

t = 12345, 54321, 'hello!'

print (t[0])
u = t, (1, 2, 3, 4, 5)
print(u)
print (t[0])

singleton = 'hello',1,3,4,66,77    
print (len(singleton))
print (singleton)
x,y,z,qq,ww,rr=singleton   # Unpacking of a tuple
print (rr)
t1 = 12345, 54321, 'hello!'
for z in t1:
    print ("Value to tup is ",z)
t2=[1,2,4,5,6]
print (type (t2))
print(t2[2:5]) 