import sys
while True:
    operation=''
    while operation not in ['1','2','3','4','5','6']:
        print ("""Select Operation 
            1. Addition
            2. Substraction
            3. Multiplication
            4. Division
            5. Exit """)
        operation=input()
    if (operation=='5'):
        sys.exit()  # This will exit the Python interpreter
    operation_lamdas={
        '1': lambda x,y:x+y,
        '2': lambda x,y:x-y,
        '3': lambda x,y:x*y,
        '4': lambda x,y:x/y
    }
    num1=''
    print ("Enter 1st number: ")
    while (not num1.isnumeric()):
        num1 = input()
    num2=' ' 
    print ("Enter 2nd number: ")
    while (not num2.isnumeric()):
        num2 = input()
    print (operation_lamdas[operation](int(num1),int(num2)))
    
