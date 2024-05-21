numbers=[1,2,3,4,5,66,77.167,77.16,77.17,22,55,6,7,8,9]
numbers.append(1) # adds to the end of the list
numbers.sort(key=abs)
print (numbers)
for yy in numbers:
    print (yy)
numbers.sort(reverse=True)
print(numbers)
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
fruits.sort()
print("Sorted fruits : ", fruits)
sorted(fruits)
print("Sorted fruits : ", fruits)
fruits.pop() # removed items from the end of the list
print(fruits)
fruits.pop()
print(fruits)

"""List Comprehensions"""

squares = [2]
for x in range(10):
    squares.append(x**2)
print(squares)

""""map() is a built-in function used to apply a function 
to each item in an iterable (like a list, tuple, etc.) 
and return an iterator that yields the results. """
print (list(map (lambda x:x +1,[2,3,4])))

m1=map (lambda x:x**2,[2,3,4])
print (list (m1)[2])
