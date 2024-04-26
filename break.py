import time
totaltime,a = 5 * 60,1
print ("This will end after "+str(totaltime)+" seconds")
while (a<=totaltime):
    print (a)
    time.sleep(1)
    a +=1