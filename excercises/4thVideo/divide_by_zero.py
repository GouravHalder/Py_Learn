operation_divide={"divide":lambda x,y:x/y}

x=''
y=''
try:
    while (not x.isnumeric()):
        x=input("Enter the first Number: ")
    while (not y.isnumeric()):
        y=input("Enter the second Number: ")
    print(operation_divide["divide"](int(x),int(y)))
except ZeroDivisionError as e:
    print("ZeroDivisionError Error caught",e)
    #raise e
except Exception as e:
    print(e)
    #raise e
finally:
    print ("In finally block")
