from math_packages import add,subtract
print (add.perform(10,5))
print (subtract.perform(10,5))
from math_packages import _private_function #Bad Practise
print (_private_function())
numbers=[1,2,3,4]
if __name__ == "__main__":
    print(numbers)
    import math_packages
    print (math_packages.foo)
    print (math_packages.__path__)
    print (math_packages.__package__)