def fib (n):
    a,b=0,1
    while (a<n):
        print (a,end=" ")
        a,b=b,a+b

def heelo_world (name='GH'):
    print (f"Hello {name}") # Concept of f Strings
fib(10)
heelo_world("bombie")
foo=heelo_world
foo("Trombie")

i = 5

def f(arg=i):
    print(arg)

i = 6
f()

def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))
print(f(4,[]))
print(f(5))