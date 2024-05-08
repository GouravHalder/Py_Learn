n=10
def add(a: int,b: int) -> int:
    from general.test_mod import fruits
    print (fruits)
    return a+b+n
def sub(a,b):
    return a-b
print(__name__)

"""To test changes to this import module 2 options
1. Restart the imterpretor
2. >>> import importlib; RUN this in the console
   >>> importlib.reload(general.my_modules)
 the """