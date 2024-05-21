class my_class:
    """This is my 1st py class"""
    foo=10
    def __init__(self,val) -> None:
        print ("In __init__")
        self.foo=val # Used to call the member varialble of the const.
        #foo=60
    def print():
        print ("In print()")
        #global foo 
        #foo=20
        #print ("In Method value of foo is: ", foo)
        #def inner_f():
         #   foo=30
          #  print ("In Inner Method value of foo is: ", foo)
        #inner_f()

#print (my_class.__doc__)
print (my_class.foo)
print (my_class.print())
my_class.foo=40
print (my_class.foo)
x=my_class(100)
print (x.foo)
x.foo=50
print (x.foo)
print (my_class.foo)
x.bombie=1000
print(x.bombie)
print (x.__dict__)
del x.foo
print (x.__dict__)
x.print()