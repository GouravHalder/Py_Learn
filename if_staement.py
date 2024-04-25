 

name = input("Please name: ")
print (name)

age = int (input("Please age: "))
print (age)

if age > 20:
    print ("Hello "+name+"  your age is "+str(age))
elif age==10:
    print("Perfect 10 years")
else:
    print ("Hello "+name + "your age is less than 20")