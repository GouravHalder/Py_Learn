foo="Heelo in __init__ foo"
def addinclass(a, b):
    print("In addinclass method")
    return a + b

def _private_function():
    print("This is a private function")

__all__=['add','subtract','addinclass']

