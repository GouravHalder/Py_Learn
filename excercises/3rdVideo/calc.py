import sys
import math
def switch_case (case):
    print ("casing ",case)
    print ("Enter 1st number: ")
    num1 = int (input())
    print ("Enter 2nd number: ")
    num2 = int (input())
    if case == 1:
        print("Addition")
        print("Result is: ",num1 + num2)
    elif case == 2:
        print("Substraction")
        print("Result is: ",num1 - num2)
    elif case == 3:
        print("Multiplication")
        print("Result is: ",num1 * num2)
    elif case == 4:
        print("Division")
        if (num1==0 or num2==0):
            print("Divide by 0 is nmot possible")
        else:
            print("Result is: ",num1 / num2)
    elif case == 5:
        print("Modulo")
        print("Result is: ",num1 % num2)   
    elif case == 6:
        print("Exponentiation")
        print("Result is: ",num1 ** num2)   
    else:
        print("Bad option")
        sys.exit()  # This will exit the Python interpreter
while True:
    print ("""Select Operation 
           1. Addition
           2. Substraction
           3. Multiplication
           4. Division
           5. Modulo
           6. Exponentiation
           Enter anything else to Exit""")
    casing = input()
    casing=int(casing)
    if (casing not in [1,2,3,4,5,6]):
        print("Exiting")
        sys.exit()  # This will exit the Python interpreter
    else:
        switch_case (casing)
