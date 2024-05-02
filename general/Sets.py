"""set is an unordered collection with no duplicate elements"""
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket) 
yy='orange' in basket  
print (yy)

a = set('abcdef')
b = set('efijkl')
print (a)
print (b)
print (a - b) 
print (a | b )      
print (a & b)
print (a ^ b  )      
