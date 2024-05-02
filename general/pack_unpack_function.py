#def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2): 

def pack(*args):
    print (args)
pack("earth", "mars", "venus","earth", "mars", "venus")

def unpack(arg1,arg2,arg3):
    print (arg1)
    print (arg2)
    print (arg3)
unpack(*range(1,4))