from dataclasses import dataclass
@dataclass
class Person:
    first_name: str
    last_name: str
    age: int
    def print(self):
        print (f'last name {self.last_name}' )
x=Person('Gourav','Halder',43)
print (x)
method=x.print
# Accessing the attributes of the method object
print(f'method.__self__: {method.__self__}')  # This should be the instance 'p'
print(f'method.__self__ is p: {method.__self__ is x}')  # Should be True
print(f'method.__func__: {method.__func__}')  # This should be the function object implementing 'print_name'
