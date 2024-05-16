my_dict={}
print ("Enter a sentence")
sen=input()
tokens=sen.split()
print ("Number of workds in the sentence is ",len(tokens))
for token in tokens:
    token=token.upper()
    if token not in my_dict:
         my_dict[token]=1
    else:
        my_dict[token]=(int(my_dict[token])) + 1

print ("Dict is ",my_dict)
print ("Word Frequencies")
for x,y in my_dict.items():
    print (x,y)