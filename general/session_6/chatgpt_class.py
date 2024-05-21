class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def print_name(self):
        print(f'{self.first_name} {self.last_name}')

# Create an instance of Person
p = Person('John', 'Doe')

# Get the print_name method object
method = p.print_name

# Accessing the attributes of the method object
print(f'method.__self__: {method.__self__}')  # This should be the instance 'p'
print(f'method.__self__ is p: {method.__self__ is p}')  # Should be True
print(f'method.__func__: {method.__func__}')  # This should be the function object implementing 'print_name'

# Call the method to see its effect
method()
