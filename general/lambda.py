def make_incrementor(n):
    return lambda x: x + n

f = make_incrementor(42)

print (f(0));
print (f(2));

val= lambda a: "Heelo" + "How are you" + str(a)
print (val(10))

pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])

print(pairs)

def kkk(x,y):
    return lambda x,y:x+y
vv= kkk("ee",3) # This assigns a lambda function to vv
vvv=vv(1,2)# This calls the lambda function with arguments 1 and 2
print ("vv is ",vvv)
print ("-----")