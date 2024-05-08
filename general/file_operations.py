with open ('../README.md',encoding='utf-8') as f:
    #print (f.read())
    #print (f.readline())
    for line in f:
        print (line)
        print ("-----------")
print ("Is the file closed? ",f.closed) # Since the file was opened using a with statement, it should be automatically closed after the block 

with open ('../Java_to_Py.md','w',encoding='utf-8') as f:
    f.write("Learning Python as a Java developer\n")
    print (f.write("from youtube")) # f.write(string) writes the contents of string to the file, returning the number of characters written.
with open ('../del_Java_to_Py.md','w',encoding='utf-8') as f:
    value = ('ab', 42)
    s = str(value)  # convert the tuple to string
    print (s)
    print ("Counting chars written ",f.write(s)) 