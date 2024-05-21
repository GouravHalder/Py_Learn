class my_class:
    foo=10
    def __init__(self,val) -> None:
        print ("In __init__",val)
        self.foo=val
        self.myprint()
    def myprint(self):
        print ("In print()")
        
x=my_class(100)
print (x.foo)
del x.foo
print (x.foo)
