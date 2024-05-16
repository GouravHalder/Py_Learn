import random

random_number = random.randint(0,100)
limit =0
while (limit < 3):
    print ("Guess your number (3 chances) ")
    your_no=int(input())
    limit=limit+1
    if (your_no < random_number):
        print ("Your number is low")
    elif (your_no > random_number):
        print ("Your number is high")
    else:
        print ("Your number is accurate")
        break
else:
    print(f"{random_number} was the Random number ")