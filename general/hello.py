print ('Hello Python')
my_boolean_variable = True

if my_boolean_variable:
    print ('my_boolean_variable is True')

text = "Python is awesome"
new_text = text.replace("awesome", "great")
print("Modified text:", new_text)
String_split = text.split();
print("Words:", String_split);

text = "   Some spaces around   "
stripped_text = text.strip()
print("Stripped text:", stripped_text)

testing="gh"*5
print (testing)

arn="111.222/3333#55555";
print ((arn.split("#"))[1]);


for i in range(2,3):
    print(i)

print(list(range(2, 10)))

num1=4
num2=5
num3 = num1 + num2
print(num3)

num100='6'
if (num100.isnumeric()):
    print ("num100 is numeric")
else:
    print ("num100 is NOT numeric")


um1=''
print ("Enter 1st number: ")
while (not um1.isnumeric()):
    um1 = input()
print (um1)

