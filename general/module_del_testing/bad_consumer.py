import import_me

def print_all():
    del import_me.foo # deletes the value from the source module itself
    print (import_me.bar)