foo=10

def sample():
    foo=20
    def inner_sample():
        nonlocal foo # nonlocal foo declares that foo refers to the foo variable in the nearest enclosing scope, which is the local scope of sample.
        foo=40
    inner_sample()
    return foo

print(sample())
print (foo)