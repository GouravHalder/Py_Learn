names =["a","b","c"]
for x in names:
    print (x , end=",") # end avoids newline 

for n in range(2, 10):
    print ("n is ",n)
    for x in range(2, n):
        print ("x is ",x)
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')