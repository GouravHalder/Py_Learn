while True:
    try:
        x=int (input("Please enter a number\n"))
        break
    except ValueError:
        print ("Enter a number dear")
    except KeyboardInterrupt:
        print ("No Cntrl+C")
        raise

try:
    raise ZeroDivisionError('foo','too')
except ZeroDivisionError as er:
    print ("Divide by 0 happened")
    print (type(er.args))# arguments stored in .args        
    print(er) # __str__ allows args to be printed directly,
    a,b= er.args
    print (a)
    print (b)


import sys

try:
    print (".........Exception Chaining............")
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error:", err)
    raise RuntimeError from None # Raising a RuntimeError from None means that you're explicitly raising the RuntimeError exception, but not specifying another exception as its cause. 
except ValueError:
    print("Could not convert data to an integer.")
except Exception as err:
    print(f"Unexpected {err=}, {type(err)=}")
    raise