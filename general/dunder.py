""""Dunder" in Python refers to "double underscore" (__) names. 
These are special methods or attributes in Python classes that have a special meaning or behavior
__init__ is a dunder method used as a constructor in Python classes
__str__ is used to define a string representation of an object when str() is called on it
__add__ is used to define the behavior of the + operator when used with objects of that class."""

class MyClass:
    def __init__(self, value):
        print ("In __init__")
        self.value = value

    def __str__(self):
        print ("In __str__")
        return f"MyClass instance with value: {self.value}"

    def __add__(self, other):
        print ("In __add__")
        return MyClass(self.value + other.value)

obj1 = MyClass(5)
obj2 = MyClass(10)

print(obj1)  # Output: MyClass instance with value: 5
print(obj1 + obj2)  # Output: MyClass instance with value: 15